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

import six

from ..api_client import ApiClient
from ..signer import Signer
missing_param = object()


class IdentityApi(object):

    def __init__(self, config):
        signer = Signer(config.tenancy, config.user, config.fingerprint, config.key_file)
        self.api_client = ApiClient(config, signer)

    def add_user_to_group(self, add_user_to_group_details, **kwargs):
        """
        AddUserToGroup
        Adds the specified user to the specified group and returns a `UserGroupMembership` object with its own OCID.\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the\nobject, first make sure its `lifecycleState` has changed to ACTIVE.\n

        :param AddUserToGroupDetails add_user_to_group_details: Request object for adding a user to a group. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type UserGroupMembership
        """
        resource_path = "/userGroupMemberships/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "add_user_to_group_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "add_user_to_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=add_user_to_group_details,
            response_type="UserGroupMembership")

    def create_compartment(self, create_compartment_details, **kwargs):
        """
        CreateCompartment
        Creates a new compartment in your tenancy. A compartment is a collection of related resources that can\nbe accessed only by certain groups that have been given permission in a policy. For conceptual\ninformation about compartments and other IAM Service components,\nsee [Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm).\n\n**Important:** Compartments cannot be renamed or deleted.\n\nYou must specify your tenancy's OCID as the compartment ID in the request object. Remember that the tenancy\nis simply the root compartment. For information about OCIDs, see\n[Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou must also specify a *name* for the compartment, which must be unique across all compartments in\nyour tenancy and cannot be changed. You can use this name or the OCID when writing policies that apply\nto the compartment. For more information about policies, see\n[How Policies Work](/Content/Identity/Concepts/policies.htm).\n\nYou must also specify a *description* for the compartment (although it can be an empty string). It does\nnot have to be unique, and you can change it anytime with [UpdateCompartment](#/en/identity/20160918/Compartment/UpdateCompartment).\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the\nobject, first make sure its `lifecycleState` has changed to ACTIVE.\n\nTo place a resource in a compartment, simply specify the compartment ID in the \"Create\" request object when\ninitially creating the resource. For example, to launch an instance into a particular compartment, specify\nthat compartment's OCID in the `LaunchInstance` request. You can't move an existing resource from one\ncompartment to another.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized, \ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see \n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n\nFor information about endpoints and signing API requests,\nsee [Making API Requests](/Content/API/Concepts/usingapi.htm).\n

        :param CreateCompartmentDetails create_compartment_details: Request object for creating a new compartment. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Compartment
        """
        resource_path = "/compartments/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_compartment_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_compartment_details,
            response_type="Compartment")

    def create_group(self, create_group_details, **kwargs):
        """
        CreateGroup
        Creates a new group in your tenancy. A group is a container for users who all need similar access to a set of resources.\nFor conceptual information about groups and other IAM Service components,\nsee [Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm).\n\nYou must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy\nis simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) \nreside within the tenancy itself, unlike cloud resources such as compute instances, which typically \nreside within compartments inside the tenancy. For information about OCIDs, see\n[Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou must also specify a *name* for the group, which must be unique across all groups in your tenancy and\ncannot be changed. You can use this name or the OCID when writing policies that apply to the group. For more\ninformation about policies, see [How Policies Work](/Content/Identity/Concepts/policies.htm).\n\nYou must also specify a *description* for the group (although it can be an empty string). It does not\nhave to be unique, and you can change it anytime with [UpdateGroup](#/en/identity/20160918/Group/UpdateGroup).\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first\nmake sure its `lifecycleState` has changed to ACTIVE.\n\nAfter creating the group, you need to put users in it and write policies for it.\nSee [AddUserToGroup](#/en/identity/20160918/UserGroupMembership/AddUserToGroup) and [CreatePolicy](#/en/identity/20160918/Policy/CreatePolicy).\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized, \ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see \n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n\nFor information about endpoints and signing API requests, see\n[Making API Requests](/Content/API/Concepts/usingapi.htm).\n

        :param CreateGroupDetails create_group_details: Request object for creating a new group. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Group
        """
        resource_path = "/groups/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_group_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_group_details,
            response_type="Group")

    def create_or_reset_ui_password(self, user_id, **kwargs):
        """
        CreateOrResetUIPassword
        Creates a new Console one-time password for the specified user. For more information about user\ncredentials, see [User Credentials](/Content/Identity/Concepts/usercredentials.htm).\n\nUse this operation after creating a new user, or if a user forgets their password. The new one-time\npassword is returned to you in the response, and you must securely deliver it to the user. They'll\nbe prompted to change this password the next time they sign in to the Console. If they don't change\nit within 7 days, the password will expire and you'll need to create a new one-time password for the\nuser. \n\n**Note:** The user's Console login is the unique name you specified when you created the user\n(see [CreateUser](#/en/identity/20160918/User/CreateUser)).\n

        :param str user_id: The user's OCID. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type UIPassword
        """
        resource_path = "/users/{userId}/uiPassword"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "user_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_or_reset_ui_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="UIPassword")

    def create_policy(self, create_policy_details, **kwargs):
        """
        CreatePolicy
        Creates a new policy in the specified compartment (either the tenancy or another of your compartments).\nA policy is a document that specifies the type of access a group has to the resources in a compartment. \nFor information about policies and other IAM Service components,\nsee [Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm).\n\nYou must specify a *name* for the policy, which must be unique across all policies in your tenancy\nand cannot be changed.\n\nYou must also specify a *description* for the policy (although it can be an empty string). It does not\nhave to be unique, and you can change it anytime with [UpdatePolicy](#/en/identity/20160918/Policy/UpdatePolicy).\n\nYou must specify one or more policy statements in the statements array. For information about writing\npolicies, see [How Policies Work](/Content/Identity/Concepts/policies.htm).\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the\nobject, first make sure its `lifecycleState` has changed to ACTIVE.\n\nNew policies take effect typically within 10 seconds.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized, \ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see \n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n\nFor information about endpoints and signing API requests,\nsee [Making API Requests](/Content/API/Concepts/usingapi.htm).\n

        :param CreatePolicyDetails create_policy_details: Request object for creating a new policy. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Policy
        """
        resource_path = "/policies/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_policy_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_policy got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_policy_details,
            response_type="Policy")

    def create_swift_password(self, create_swift_password_details, user_id, **kwargs):
        """
        CreateSwiftPassword
        Creates a new Swift password for the specified user. A user can have up to two Swift passwords at a time. Swift\npasswords never expire. For information about what Swift passwords are for, see\n[Managing User Credentials](/Content/Identity/Tasks/managingcredentials.htm).\n\nYou must specify a *description* for the Swift password (although it can be an empty string). It does not\nhave to be unique, and you can change it anytime with [UpdateSwiftPassword](#/en/identity/20160918/SwiftPassword/UpdateSwiftPassword).\n\nEvery user has permission to create a Swift password for *their own user ID*. An administrator in your organization\ndoes not need to write a policy to give users this ability. To compare, administrators who have permission to the\ntenancy can use this operation to create a Swift password for any user, including themselves.\n

        :param CreateSwiftPasswordDetails create_swift_password_details: Request object for creating a new swift password. (required)
        :param str user_id: The user's OCID. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type SwiftPassword
        """
        resource_path = "/users/{userId}/swiftPasswords/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_swift_password_details",
            "user_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_swift_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=create_swift_password_details,
            response_type="SwiftPassword")

    def create_user(self, create_user_details, **kwargs):
        """
        CreateUser
        Creates a new user in your tenancy. For conceptual information about users, your tenancy, and other\nIAM Service components, see [Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm).\n\nYou must specify your tenancy's OCID as the compartment ID in the request object (remember that the\ntenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) \nreside within the tenancy itself, unlike cloud resources such as compute instances, which typically \nreside within compartments inside the tenancy. For information about OCIDs, see\n[Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou must also specify a *name* for the user, which must be unique across all users in your tenancy\nand cannot be changed. If you specify a name that's already in use, you'll get a 409 error.\nThis name will be the user's login to the Console. You might want to pick a\nname that your company's own identity system (e.g., Active Directory, LDAP, etc.) already uses.\nIf you delete a user and then create a new user with the same name, they'll be considered different\nusers because they have different OCIDs.\n\nYou must also specify a *description* for the user (although it can be an empty string).\nIt does not have to be unique, and you can change it anytime with [UpdateUser](#/en/identity/20160918/User/UpdateUser).\nYou can use the field to provide the user's full name, a description, a nickname, or other\ninformation to generally identify the user.\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the\nobject, first make sure its `lifecycleState` has changed to ACTIVE.\n\nA new user has no permissions until you place the user in one or more groups (see\n[AddUserToGroup](#/en/identity/20160918/UserGroupMembership/AddUserToGroup). If the user needs to access the Console, you need to\nprovide the user a password (see [CreateOrResetUIPassword](#/en/identity/20160918/UIPassword/CreateOrResetUIPassword)).\nIf the user needs to access the Oracle Bare Metal Cloud REST API, you need to upload a public API signing\nkey for that user (see [UploadApiKey](#/en/identity/20160918/ApiKey/UploadApiKey)).\n\n**Important:** Make sure to inform the new user which compartment(s) they have access to. \n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized, \ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see \n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n\nFor information about endpoints and signing API requests,\nsee [Making API Requests](/Content/API/Concepts/usingapi.htm).\n

        :param CreateUserDetails create_user_details: Request object for creating a new user. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type User
        """
        resource_path = "/users/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_user_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_user got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_user_details,
            response_type="User")

    def delete_api_key(self, user_id, fingerprint, **kwargs):
        """
        DeleteApiKey
        Deletes the specified API signing key for the specified user.\n\nEvery user has permission to use this operation to delete a key for *their own user ID*. An\nadministrator in your organization does not need to write a policy to give users this ability.\nTo compare, administrators who have permission to the tenancy can use this operation to delete\na key for any user, including themselves.\n

        :param str user_id: The user's OCID. (required)
        :param str fingerprint: The key's fingerprint. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/users/{userId}/apiKeys/{fingerprint}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "user_id",
            "fingerprint",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_api_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "fingerprint": fingerprint
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_group(self, group_id, **kwargs):
        """
        DeleteGroup
        Deletes the specified group. The group must be empty.\n

        :param str group_id: The group's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/groups/{groupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "group_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "groupId": group_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_policy(self, policy_id, **kwargs):
        """
        DeletePolicy
        Deletes the specified policy. The deletion takes effect typically within 10 seconds.

        :param str policy_id: The policy's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/policies/{policyId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "policy_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyId": policy_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_swift_password(self, user_id, swift_password_id, **kwargs):
        """
        DeleteSwiftPassword
        Deletes the specified Swift password for the specified user.\n

        :param str user_id: The user's OCID. (required)
        :param str swift_password_id: The Swift password's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/users/{userId}/swiftPasswords/{swiftPasswordId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "user_id",
            "swift_password_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_swift_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "swiftPasswordId": swift_password_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_user(self, user_id, **kwargs):
        """
        DeleteUser
        Deletes the specified user. The user must not be in any groups.

        :param str user_id: The user's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/users/{userId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "user_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def get_compartment(self, compartment_id, **kwargs):
        """
        GetCompartment
        Gets the specified compartment's information.\n\nThis operation does not return a list of all the resources inside the compartment. There is no single\nAPI operation that does that. Compartments can contain multiple types of resources (instances, block\nstorage volumes, etc.). To find out what's in a compartment, you must call the \"List\" operation for\neach resource type and specify the compartment's OCID as a query parameter in the request. For example,\ncall the `ListInstances` operation in the Cloud Compute Service or the `ListVolumes` operation in\nCloud Block Storage.\n

        :param str compartment_id: The compartment's OCID. (required)
        :return: A Response object with data of type Compartment
        """
        resource_path = "/compartments/{compartmentId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "compartmentId": compartment_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Compartment")

    def get_group(self, group_id, **kwargs):
        """
        GetGroup
        Gets the specified group's information.\n\nThis operation does not return a list of all the users in the group. To do that, use\n[ListUserGroupMemberships](#/en/identity/20160918/UserGroupMembership/ListUserGroupMemberships) and provide the group's OCID as a\nquery parameter in the request.\n

        :param str group_id: The group's OCID. (required)
        :return: A Response object with data of type Group
        """
        resource_path = "/groups/{groupId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "group_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "groupId": group_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Group")

    def get_policy(self, policy_id, **kwargs):
        """
        GetPolicy
        Gets the specified policy's information.

        :param str policy_id: The policy's OCID. (required)
        :return: A Response object with data of type Policy
        """
        resource_path = "/policies/{policyId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "policy_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyId": policy_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Policy")

    def get_user(self, user_id, **kwargs):
        """
        GetUser
        Gets the specified user's information.

        :param str user_id: The user's OCID. (required)
        :return: A Response object with data of type User
        """
        resource_path = "/users/{userId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "user_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="User")

    def get_user_group_membership(self, user_group_membership_id, **kwargs):
        """
        GetUserGroupMembership
        Gets the specified UserGroupMembership's information.

        :param str user_group_membership_id: The userGroupMembership's OCID. (required)
        :return: A Response object with data of type UserGroupMembership
        """
        resource_path = "/userGroupMemberships/{userGroupMembershipId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "user_group_membership_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_user_group_membership got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userGroupMembershipId": user_group_membership_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="UserGroupMembership")

    def list_api_keys(self, user_id, **kwargs):
        """
        ListApiKeys
        Gets a list of the API signing keys for the specified user. A user can have a maximum of three keys.\n\nEvery user has permission to use this API call for *their own user ID*.  An administrator in your\norganization does not need to write a policy to give users this ability.\n

        :param str user_id: The user's OCID. (required)
        :return: A Response object with data of type list[ApiKey]
        """
        resource_path = "/users/{userId}/apiKeys/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "user_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_api_keys got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="list[ApiKey]")

    def list_availability_domains(self, compartment_id, **kwargs):
        """
        ListAvailabilityDomains
        Gets a list of all the Availability Domains in your tenancy. Specify the OCID of either the tenancy or another\nof your compartments as the value for the compartment ID (remember that the tenancy is simply the root compartment).\nSee [Where to Find Your Tenancy's OCID](/Content/API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID).\nFor information about Availability Domains, see\n[Regions and Availability Domains](/Content/General/Concepts/regions.htm).\n\nFor information about endpoints and signing API requests,\nsee [Making API Requests](/Content/API/Concepts/usingapi.htm).\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :return: A Response object with data of type list[AvailabilityDomain]
        """
        resource_path = "/availabilityDomains/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_availability_domains got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[AvailabilityDomain]")

    def list_compartments(self, compartment_id, **kwargs):
        """
        ListCompartments
        Gets a list of all the compartments in your tenancy. You must specify your tenancy's OCID as the value\nfor the compartment ID (remember that the tenancy is simply the root compartment).\nSee [Where to Find Your Tenancy's OCID](/Content/API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID).\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized, \ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see \n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n
        :return: A Response object with data of type list[Compartment]
        """
        resource_path = "/compartments/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_compartments got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing_param),
            "limit": kwargs.get("limit", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Compartment]")

    def list_groups(self, compartment_id, **kwargs):
        """
        ListGroups
        Gets a list of all the groups in your tenancy. You must specify your tenancy's OCID as the value for\nthe compartment ID (remember that the tenancy is simply the root compartment).\nSee [Where to Find Your Tenancy's OCID](/Content/API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID).\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized, \ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see \n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n
        :return: A Response object with data of type list[Group]
        """
        resource_path = "/groups/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_groups got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing_param),
            "limit": kwargs.get("limit", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Group]")

    def list_policies(self, compartment_id, **kwargs):
        """
        ListPolicies
        Gets a list of all the policies in the specified compartment (either the tenancy or another of your compartments). \nSee [Where to Find Your Tenancy's OCID](/Content/API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID).\n\nTo determine which policies apply to a particular group or compartment, you must view the individual\nstatements inside all your policies. There isn't a way to automatically obtain that information via the API.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized, \ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see \n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n
        :return: A Response object with data of type list[Policy]
        """
        resource_path = "/policies/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_policies got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing_param),
            "limit": kwargs.get("limit", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Policy]")

    def list_swift_passwords(self, user_id, **kwargs):
        """
        ListSwiftPasswords
        Gets a list of the Swift passwords for the specified user. The returned object contains the password's OCID, but not\nthe password itself. The actual password is returned only upon creation. A user can have up to two Swift passwords at\na time.\n

        :param str user_id: The user's OCID. (required)
        :return: A Response object with data of type list[SwiftPassword]
        """
        resource_path = "/users/{userId}/swiftPasswords/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "user_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_swift_passwords got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="list[SwiftPassword]")

    def list_user_group_memberships(self, compartment_id, **kwargs):
        """
        ListUserGroupMemberships
        Gets a list of all the `UserGroupMembership` objects in your tenancy. You must specify your tenancy's OCID\nas the value for the compartment ID\n(see [Where to Find Your Tenancy's OCID](/Content/API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID)).\nYou must also then filter the list in one of these ways:\n\n- You can limit the results to just the memberships for a given user by specifying a `userId`.\n- Similarly, you can limit the results to just the memberships for a given group by specifying a `groupId`.\n- You can set both the `userId` and `groupId` to determine if the specified user is in the specified group.\nIf the answer is no, the response is an empty list.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized, \ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see \n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :param str user_id: The user's OCID.
        :param str group_id: The group's OCID.
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n
        :return: A Response object with data of type list[UserGroupMembership]
        """
        resource_path = "/userGroupMemberships/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "user_id",
            "group_id",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_user_group_memberships got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "userId": kwargs.get("user_id", missing_param),
            "groupId": kwargs.get("group_id", missing_param),
            "page": kwargs.get("page", missing_param),
            "limit": kwargs.get("limit", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[UserGroupMembership]")

    def list_users(self, compartment_id, **kwargs):
        """
        ListUsers
        Gets a list of all the users in your tenancy. You must specify your tenancy's OCID as the value for the\ncompartment ID (remember that the tenancy is simply the root compartment).\nSee [Where to Find Your Tenancy's OCID](/Content/API/Concepts/usingapi.htm#Where_to_Find_Your_Tenancy's_OCID).\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized, \ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see \n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: Your tenancy's OCID (remember that the tenancy is simply the root compartment).\n (required)
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n
        :return: A Response object with data of type list[User]
        """
        resource_path = "/users/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_users got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing_param),
            "limit": kwargs.get("limit", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[User]")

    def remove_user_from_group(self, user_group_membership_id, **kwargs):
        """
        RemoveUserFromGroup
        Removes a user from a group by deleting the corresponding `UserGroupMembership`.

        :param str user_group_membership_id: The userGroupMembership's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/userGroupMemberships/{userGroupMembershipId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "user_group_membership_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "remove_user_from_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userGroupMembershipId": user_group_membership_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def update_compartment(self, compartment_id, update_compartment_details, **kwargs):
        """
        UpdateCompartment
        Updates the specified compartment.

        :param str compartment_id: The compartment's OCID. (required)
        :param UpdateCompartmentDetails update_compartment_details: Request object for updating a compartment. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type Compartment
        """
        resource_path = "/compartments/{compartmentId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "update_compartment_details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "compartmentId": compartment_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_compartment_details,
            response_type="Compartment")

    def update_group(self, group_id, update_group_details, **kwargs):
        """
        UpdateGroup
        Updates the specified group.

        :param str group_id: The group's OCID. (required)
        :param UpdateGroupDetails update_group_details: Request object for updating a group. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type Group
        """
        resource_path = "/groups/{groupId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "group_id",
            "update_group_details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "groupId": group_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_group_details,
            response_type="Group")

    def update_policy(self, policy_id, update_policy_details, **kwargs):
        """
        UpdatePolicy
        Updates the specified policy.\n\nPolicy changes take effect typically within 10 seconds.\n

        :param str policy_id: The policy's OCID. (required)
        :param UpdatePolicyDetails update_policy_details: Request object for updating a policy. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type Policy
        """
        resource_path = "/policies/{policyId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "policy_id",
            "update_policy_details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyId": policy_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_policy_details,
            response_type="Policy")

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
        resource_path = "/users/{userId}/swiftPasswords/{swiftPasswordId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "user_id",
            "swift_password_id",
            "update_swift_password_details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_swift_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "swiftPasswordId": swift_password_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_swift_password_details,
            response_type="SwiftPassword")

    def update_user(self, user_id, update_user_details, **kwargs):
        """
        UpdateUser
        Updates the specified user.

        :param str user_id: The user's OCID. (required)
        :param UpdateUserDetails update_user_details: Request object for updating a user. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type User
        """
        resource_path = "/users/{userId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "user_id",
            "update_user_details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_user_details,
            response_type="User")

    def update_user_state(self, user_id, update_state_details, **kwargs):
        """
        UpdateUserState
        Updates the state of the specified user.

        :param str user_id: The user's OCID. (required)
        :param UpdateStateDetails update_state_details: Request object for updating a user state. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type User
        """
        resource_path = "/users/{userId}/state/"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "user_id",
            "update_state_details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_user_state got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_state_details,
            response_type="User")

    def upload_api_key(self, user_id, create_api_key_details, **kwargs):
        """
        UploadApiKey
        Uploads an API signing key for the specified user.  Each user can have a maximum of three keys.\nEach key must be an RSA public key in PEM format. For more information about the format and how\nto generate a key, see [Generating an API Signing Key](/Content/API/Concepts/apisigningkey.htm). For more\ninformation about user credentials, see [User Credentials](/Content/Identity/Concepts/usercredentials.htm).\n\nEvery user has permission to use this operation to upload a key for *their own user ID*. An\nadministrator in your organization does not need to write a policy to give users this ability.\nTo compare, administrators who have permission to the tenancy can use this operation to upload a\nkey for any user, including themselves.\n\n**Important:** Even though you have permission to upload an API key, you might not yet\nhave permission to do much else. If you try calling an operation unrelated to your own credential\nmanagement (e.g., `ListUsers`, `LaunchInstance`) and receive an \"unauthorized\" error,\ncheck with an administrator to confirm which IAM Service group(s) you're in and what permissions\nyou have. Also confirm you're working in the correct compartment. \n\n**Note:** The resulting `ApiKey` object includes a placeholder, Oracle-assigned description.\nYou can't set or change that value.\n\nAfter you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using\nthe object, first make sure its `lifecycleState` has changed to ACTIVE.\n

        :param str user_id: The user's OCID. (required)
        :param CreateApiKeyDetails create_api_key_details: Request object for uploading an API key for a user. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type ApiKey
        """
        resource_path = "/users/{userId}/apiKeys/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "user_id",
            "create_api_key_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "upload_api_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_identity_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=create_api_key_details,
            response_type="ApiKey")
