# coding: utf-8
# Copyright (c) 2017 Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

import six

from ..base_client import BaseClient
from ..config import validate_config
from ..signer import Signer
from ..util import Sentinel
from .models import identity_type_mapping
missing = Sentinel("Missing")


class IdentityClient(object):

    def __init__(self, config):
        validate_config(config)
        signer = Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config["key_file"],
            pass_phrase=config["pass_phrase"]
        )
        self.base_client = BaseClient("identity", config, signer, identity_type_mapping)

    def add_user_to_group(self, add_user_to_group_details, **kwargs):
        """
        AddUserToGroup
        Adds the specified user to the specified group and returns a `UserGroupMembership` object with its own OCID.
        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
        object, first make sure its `lifecycleState` has changed to ACTIVE.

        :param AddUserToGroupDetails add_user_to_group_details: (required)
            Request object for adding a user to a group.
        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
        :return: A Response object with data of type UserGroupMembership
        """
        resource_path = "/userGroupMemberships/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "add_user_to_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=add_user_to_group_details,
            response_type="UserGroupMembership")

    def create_compartment(self, create_compartment_details, **kwargs):
        """
        CreateCompartment
        Creates a new compartment in your tenancy.
        **Important:** Compartments cannot be renamed or deleted.
        You must specify your tenancy's OCID as the compartment ID in the request object. Remember that the tenancy
        is simply the root compartment. For information about OCIDs, see
        [Resource Identifiers]({{DOC_SERVER_URL}}/Content/General/Concepts/identifiers.htm).
        You must also specify a *name* for the compartment, which must be unique across all compartments in
        your tenancy and cannot be changed. You can use this name or the OCID when writing policies that apply
        to the compartment. For more information about policies, see
        [How Policies Work]({{DOC_SERVER_URL}}/Content/Identity/Concepts/policies.htm).
        You must also specify a *description* for the compartment (although it can be an empty string). It does
        not have to be unique, and you can change it anytime with
        UpdateCompartment.
        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
        object, first make sure its `lifecycleState` has changed to ACTIVE.

        :param CreateCompartmentDetails create_compartment_details: (required)
            Request object for creating a new compartment.
        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
        :return: A Response object with data of type Compartment
        """
        resource_path = "/compartments/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_compartment_details,
            response_type="Compartment")

    def create_group(self, create_group_details, **kwargs):
        """
        CreateGroup
        Creates a new group in your tenancy.
        You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy
        is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies)
        reside within the tenancy itself, unlike cloud resources such as compute instances, which typically
        reside within compartments inside the tenancy. For information about OCIDs, see
        [Resource Identifiers]({{DOC_SERVER_URL}}/Content/General/Concepts/identifiers.htm).
        You must also specify a *name* for the group, which must be unique across all groups in your tenancy and
        cannot be changed. You can use this name or the OCID when writing policies that apply to the group. For more
        information about policies, see [How Policies Work]({{DOC_SERVER_URL}}/Content/Identity/Concepts/policies.htm).
        You must also specify a *description* for the group (although it can be an empty string). It does not
        have to be unique, and you can change it anytime with UpdateGroup.
        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
        object, first make sure its `lifecycleState` has changed to ACTIVE.
        After creating the group, you need to put users in it and write policies for it.
        See AddUserToGroup and
        CreatePolicy.

        :param CreateGroupDetails create_group_details: (required)
            Request object for creating a new group.
        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
        :return: A Response object with data of type Group
        """
        resource_path = "/groups/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_group_details,
            response_type="Group")

    def create_or_reset_ui_password(self, user_id, **kwargs):
        """
        CreateOrResetUIPassword
        Creates a new Console one-time password for the specified user. For more information about user
        credentials, see [User Credentials]({{DOC_SERVER_URL}}/Content/Identity/Concepts/usercredentials.htm).
        Use this operation after creating a new user, or if a user forgets their password. The new one-time
        password is returned to you in the response, and you must securely deliver it to the user. They'll
        be prompted to change this password the next time they sign in to the Console. If they don't change
        it within 7 days, the password will expire and you'll need to create a new one-time password for the
        user.
        **Note:** The user's Console login is the unique name you specified when you created the user
        (see CreateUser).

        :param str user_id: (required)
            The OCID of the user.
        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
        :return: A Response object with data of type UIPassword
        """
        resource_path = "/users/{userId}/uiPassword"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_or_reset_ui_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="UIPassword")

    def create_policy(self, create_policy_details, **kwargs):
        """
        CreatePolicy
        Creates a new policy in the specified compartment (either the tenancy or another of your compartments).
        If you're new to policies, see [Getting Started with Policies]({{DOC_SERVER_URL}}/Content/Identity/Concepts/policygetstarted.htm).
        You must specify a *name* for the policy, which must be unique across all policies in your tenancy
        and cannot be changed.
        You must also specify a *description* for the policy (although it can be an empty string). It does not
        have to be unique, and you can change it anytime with UpdatePolicy.
        You must specify one or more policy statements in the statements array. For information about writing
        policies, see [How Policies Work]({{DOC_SERVER_URL}}/Content/Identity/Concepts/policies.htm) and
        [Common Policies]({{DOC_SERVER_URL}}/Content/Identity/Concepts/commonpolicies.htm).
        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
        object, first make sure its `lifecycleState` has changed to ACTIVE.
        New policies take effect typically within 10 seconds.

        :param CreatePolicyDetails create_policy_details: (required)
            Request object for creating a new policy.
        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
        :return: A Response object with data of type Policy
        """
        resource_path = "/policies/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_policy got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_policy_details,
            response_type="Policy")

    def create_swift_password(self, create_swift_password_details, user_id, **kwargs):
        """
        CreateSwiftPassword
        Creates a new Swift password for the specified user. For information about what Swift passwords are for, see
        [Managing User Credentials]({{DOC_SERVER_URL}}/Content/Identity/Tasks/managingcredentials.htm).
        You must specify a *description* for the Swift password (although it can be an empty string). It does not
        have to be unique, and you can change it anytime with
        UpdateSwiftPassword.
        Every user has permission to create a Swift password for *their own user ID*. An administrator in your organization
        does not need to write a policy to give users this ability. To compare, administrators who have permission to the
        tenancy can use this operation to create a Swift password for any user, including themselves.

        :param CreateSwiftPasswordDetails create_swift_password_details: (required)
            Request object for creating a new swift password.
                :param str user_id: (required)
            The OCID of the user.
        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
        :return: A Response object with data of type SwiftPassword
        """
        resource_path = "/users/{userId}/swiftPasswords/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_swift_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=create_swift_password_details,
            response_type="SwiftPassword")

    def create_user(self, create_user_details, **kwargs):
        """
        CreateUser
        Creates a new user in your tenancy. For conceptual information about users, your tenancy, and other
        IAM Service components, see [Overview of the IAM Service]({{DOC_SERVER_URL}}/Content/Identity/Concepts/overview.htm).
        You must specify your tenancy's OCID as the compartment ID in the request object (remember that the
        tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and
        some policies) reside within the tenancy itself, unlike cloud resources such as compute instances,
        which typically reside within compartments inside the tenancy. For information about OCIDs, see
        [Resource Identifiers]({{DOC_SERVER_URL}}/Content/General/Concepts/identifiers.htm).
        You must also specify a *name* for the user, which must be unique across all users in your tenancy
        and cannot be changed. Allowed characters: No spaces. Only letters, numerals, hyphens, periods,
        underscores, +, and @. If you specify a name that's already in use, you'll get a 409 error.
        This name will be the user's login to the Console. You might want to pick a
        name that your company's own identity system (e.g., Active Directory, LDAP, etc.) already uses.
        If you delete a user and then create a new user with the same name, they'll be considered different
        users because they have different OCIDs.
        You must also specify a *description* for the user (although it can be an empty string).
        It does not have to be unique, and you can change it anytime with
        UpdateUser. You can use the field to provide the user's
        full name, a description, a nickname, or other information to generally identify the user.
        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before
        using the object, first make sure its `lifecycleState` has changed to ACTIVE.
        A new user has no permissions until you place the user in one or more groups (see
        AddUserToGroup). If the user needs to
        access the Console, you need to provide the user a password (see
        CreateOrResetUIPassword).
        If the user needs to access the Oracle Bare Metal Cloud Services REST API, you need to upload a
        public API signing key for that user (see
        [Required Keys and OCIDs]({{DOC_SERVER_URL}}/Content/API/Concepts/apisigningkey.htm) and also
        UploadApiKey).
        **Important:** Make sure to inform the new user which compartment(s) they have access to.

        :param CreateUserDetails create_user_details: (required)
            Request object for creating a new user.
        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
        :return: A Response object with data of type User
        """
        resource_path = "/users/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_user got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_user_details,
            response_type="User")

    def delete_api_key(self, user_id, fingerprint, **kwargs):
        """
        DeleteApiKey
        Deletes the specified API signing key for the specified user.
        Every user has permission to use this operation to delete a key for *their own user ID*. An
        administrator in your organization does not need to write a policy to give users this ability.
        To compare, administrators who have permission to the tenancy can use this operation to delete
        a key for any user, including themselves.

        :param str user_id: (required)
            The OCID of the user.
                :param str fingerprint: (required)
            The key's fingerprint.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type None
        """
        resource_path = "/users/{userId}/apiKeys/{fingerprint}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_api_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "fingerprint": fingerprint
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_group(self, group_id, **kwargs):
        """
        DeleteGroup
        Deletes the specified group. The group must be empty.

        :param str group_id: (required)
            The OCID of the group.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type None
        """
        resource_path = "/groups/{groupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "groupId": group_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_policy(self, policy_id, **kwargs):
        """
        DeletePolicy
        Deletes the specified policy. The deletion takes effect typically within 10 seconds.

        :param str policy_id: (required)
            The OCID of the policy.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type None
        """
        resource_path = "/policies/{policyId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyId": policy_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_swift_password(self, user_id, swift_password_id, **kwargs):
        """
        DeleteSwiftPassword
        Deletes the specified Swift password for the specified user.

        :param str user_id: (required)
            The OCID of the user.
                :param str swift_password_id: (required)
            The OCID of the Swift password.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type None
        """
        resource_path = "/users/{userId}/swiftPasswords/{swiftPasswordId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_swift_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "swiftPasswordId": swift_password_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_user(self, user_id, **kwargs):
        """
        DeleteUser
        Deletes the specified user. The user must not be in any groups.

        :param str user_id: (required)
            The OCID of the user.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type None
        """
        resource_path = "/users/{userId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def get_compartment(self, compartment_id, **kwargs):
        """
        GetCompartment
        Gets the specified compartment's information.
        This operation does not return a list of all the resources inside the compartment. There is no single
        API operation that does that. Compartments can contain multiple types of resources (instances, block
        storage volumes, etc.). To find out what's in a compartment, you must call the \"List\" operation for
        each resource type and specify the compartment's OCID as a query parameter in the request. For example,
        call the ListInstances operation in the Cloud Compute
        Service or the ListVolumes operation in Cloud Block Storage.

        :param str compartment_id: (required)
            The OCID of the compartment.
        :return: A Response object with data of type Compartment
        """
        resource_path = "/compartments/{compartmentId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_compartment got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "compartmentId": compartment_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Compartment")

    def get_group(self, group_id, **kwargs):
        """
        GetGroup
        Gets the specified group's information.
        This operation does not return a list of all the users in the group. To do that, use
        ListUserGroupMemberships and
        provide the group's OCID as a query parameter in the request.

        :param str group_id: (required)
            The OCID of the group.
        :return: A Response object with data of type Group
        """
        resource_path = "/groups/{groupId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_group got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "groupId": group_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Group")

    def get_policy(self, policy_id, **kwargs):
        """
        GetPolicy
        Gets the specified policy's information.

        :param str policy_id: (required)
            The OCID of the policy.
        :return: A Response object with data of type Policy
        """
        resource_path = "/policies/{policyId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_policy got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "policyId": policy_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Policy")

    def get_user(self, user_id, **kwargs):
        """
        GetUser
        Gets the specified user's information.

        :param str user_id: (required)
            The OCID of the user.
        :return: A Response object with data of type User
        """
        resource_path = "/users/{userId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_user got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="User")

    def get_user_group_membership(self, user_group_membership_id, **kwargs):
        """
        GetUserGroupMembership
        Gets the specified UserGroupMembership's information.

        :param str user_group_membership_id: (required)
            The OCID of the userGroupMembership.
        :return: A Response object with data of type UserGroupMembership
        """
        resource_path = "/userGroupMemberships/{userGroupMembershipId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_user_group_membership got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "userGroupMembershipId": user_group_membership_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="UserGroupMembership")

    def list_api_keys(self, user_id, **kwargs):
        """
        ListApiKeys
        Lists the API signing keys for the specified user. A user can have a maximum of three keys.
        Every user has permission to use this API call for *their own user ID*.  An administrator in your
        organization does not need to write a policy to give users this ability.

        :param str user_id: (required)
            The OCID of the user.
        :return: A Response object with data of type list[ApiKey]
        """
        resource_path = "/users/{userId}/apiKeys/"
        method = "GET"

        if kwargs:
            raise ValueError(
                "list_api_keys got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="list[ApiKey]")

    def list_availability_domains(self, compartment_id, **kwargs):
        """
        ListAvailabilityDomains
        Lists the Availability Domains in your tenancy. Specify the OCID of either the tenancy or another
        of your compartments as the value for the compartment ID (remember that the tenancy is simply the root compartment).
        See [Where to Get the Tenancy's OCID and User's OCID]({{DOC_SERVER_URL}}/Content/API/Concepts/apisigningkey.htm#five).

        :param str compartment_id: (required)
            The OCID of the compartment (remember that the tenancy is simply the root compartment).
        :return: A Response object with data of type list[AvailabilityDomain]
        """
        resource_path = "/availabilityDomains/"
        method = "GET"

        if kwargs:
            raise ValueError(
                "list_availability_domains got unknown kwargs: {!r}".format(kwargs))

        query_params = {
            "compartmentId": compartment_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[AvailabilityDomain]")

    def list_compartments(self, compartment_id, **kwargs):
        """
        ListCompartments
        Lists the compartments in your tenancy. You must specify your tenancy's OCID as the value
        for the compartment ID (remember that the tenancy is simply the root compartment).
        See [Where to Get the Tenancy's OCID and User's OCID]({{DOC_SERVER_URL}}/Content/API/Concepts/apisigningkey.htm#five).
        To use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,
        talk to an administrator. If you're an administrator who needs to write policies to give users access, see
        [Getting Started with Policies]({{DOC_SERVER_URL}}/Content/Identity/Concepts/policygetstarted.htm).

        :param str compartment_id: (required)
            The OCID of the compartment (remember that the tenancy is simply the root compartment).
        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.
        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.
        :return: A Response object with data of type list[Compartment]
        """
        resource_path = "/compartments/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_compartments got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Compartment]")

    def list_groups(self, compartment_id, **kwargs):
        """
        ListGroups
        Lists the groups in your tenancy. You must specify your tenancy's OCID as the value for
        the compartment ID (remember that the tenancy is simply the root compartment).
        See [Where to Get the Tenancy's OCID and User's OCID]({{DOC_SERVER_URL}}/Content/API/Concepts/apisigningkey.htm#five).

        :param str compartment_id: (required)
            The OCID of the compartment (remember that the tenancy is simply the root compartment).
        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.
        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.
        :return: A Response object with data of type list[Group]
        """
        resource_path = "/groups/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_groups got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Group]")

    def list_policies(self, compartment_id, **kwargs):
        """
        ListPolicies
        Lists the policies in the specified compartment (either the tenancy or another of your compartments).
        See [Where to Get the Tenancy's OCID and User's OCID]({{DOC_SERVER_URL}}/Content/API/Concepts/apisigningkey.htm#five).
        To determine which policies apply to a particular group or compartment, you must view the individual
        statements inside all your policies. There isn't a way to automatically obtain that information via the API.

        :param str compartment_id: (required)
            The OCID of the compartment (remember that the tenancy is simply the root compartment).
        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.
        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.
        :return: A Response object with data of type list[Policy]
        """
        resource_path = "/policies/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_policies got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Policy]")

    def list_swift_passwords(self, user_id, **kwargs):
        """
        ListSwiftPasswords
        Lists the Swift passwords for the specified user. The returned object contains the password's OCID, but not
        the password itself. The actual password is returned only upon creation.

        :param str user_id: (required)
            The OCID of the user.
        :return: A Response object with data of type list[SwiftPassword]
        """
        resource_path = "/users/{userId}/swiftPasswords/"
        method = "GET"

        if kwargs:
            raise ValueError(
                "list_swift_passwords got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="list[SwiftPassword]")

    def list_user_group_memberships(self, compartment_id, **kwargs):
        """
        ListUserGroupMemberships
        Lists the `UserGroupMembership` objects in your tenancy. You must specify your tenancy's OCID
        as the value for the compartment ID
        (see [Where to Get the Tenancy's OCID and User's OCID]({{DOC_SERVER_URL}}/Content/API/Concepts/apisigningkey.htm#five)).
        You must also then filter the list in one of these ways:
        - You can limit the results to just the memberships for a given user by specifying a `userId`.
        - Similarly, you can limit the results to just the memberships for a given group by specifying a `groupId`.
        - You can set both the `userId` and `groupId` to determine if the specified user is in the specified group.
        If the answer is no, the response is an empty list.
        To use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,
        talk to an administrator. If you're an administrator who needs to write policies to give users access, see
        [Getting Started with Policies]({{DOC_SERVER_URL}}/Content/Identity/Concepts/policygetstarted.htm).

        :param str compartment_id: (required)
            The OCID of the compartment (remember that the tenancy is simply the root compartment).
        :param str user_id: (optional)
            The OCID of the user.
        :param str group_id: (optional)
            The OCID of the group.
        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.
        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.
        :return: A Response object with data of type list[UserGroupMembership]
        """
        resource_path = "/userGroupMemberships/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "user_id",
            "group_id",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_user_group_memberships got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "userId": kwargs.get("user_id", missing),
            "groupId": kwargs.get("group_id", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[UserGroupMembership]")

    def list_users(self, compartment_id, **kwargs):
        """
        ListUsers
        Lists the users in your tenancy. You must specify your tenancy's OCID as the value for the
        compartment ID (remember that the tenancy is simply the root compartment).
        See [Where to Get the Tenancy's OCID and User's OCID]({{DOC_SERVER_URL}}/Content/API/Concepts/apisigningkey.htm#five).

        :param str compartment_id: (required)
            The OCID of the compartment (remember that the tenancy is simply the root compartment).
        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.
        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.
        :return: A Response object with data of type list[User]
        """
        resource_path = "/users/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_users got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[User]")

    def remove_user_from_group(self, user_group_membership_id, **kwargs):
        """
        RemoveUserFromGroup
        Removes a user from a group by deleting the corresponding `UserGroupMembership`.

        :param str user_group_membership_id: (required)
            The OCID of the userGroupMembership.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type None
        """
        resource_path = "/userGroupMemberships/{userGroupMembershipId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "remove_user_from_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userGroupMembershipId": user_group_membership_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def update_compartment(self, compartment_id, update_compartment_details, **kwargs):
        """
        UpdateCompartment
        Updates the specified compartment's description.

        :param str compartment_id: (required)
            The OCID of the compartment.
                :param UpdateCompartmentDetails update_compartment_details: (required)
            Request object for updating a compartment.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type Compartment
        """
        resource_path = "/compartments/{compartmentId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "compartmentId": compartment_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
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

        :param str group_id: (required)
            The OCID of the group.
                :param UpdateGroupDetails update_group_details: (required)
            Request object for updating a group.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type Group
        """
        resource_path = "/groups/{groupId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "groupId": group_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_group_details,
            response_type="Group")

    def update_policy(self, policy_id, update_policy_details, **kwargs):
        """
        UpdatePolicy
        Updates the specified policy. You can update the description or the policy statements themselves.
        Policy changes take effect typically within 10 seconds.

        :param str policy_id: (required)
            The OCID of the policy.
                :param UpdatePolicyDetails update_policy_details: (required)
            Request object for updating a policy.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type Policy
        """
        resource_path = "/policies/{policyId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyId": policy_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_policy_details,
            response_type="Policy")

    def update_swift_password(self, user_id, swift_password_id, update_swift_password_details, **kwargs):
        """
        UpdateSwiftPassword
        Updates the specified Swift password's description.

        :param str user_id: (required)
            The OCID of the user.
                :param str swift_password_id: (required)
            The OCID of the Swift password.
                :param UpdateSwiftPasswordDetails update_swift_password_details: (required)
            Request object for updating a Swift password.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type SwiftPassword
        """
        resource_path = "/users/{userId}/swiftPasswords/{swiftPasswordId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_swift_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "swiftPasswordId": swift_password_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_swift_password_details,
            response_type="SwiftPassword")

    def update_user(self, user_id, update_user_details, **kwargs):
        """
        UpdateUser
        Updates the description of the specified user.

        :param str user_id: (required)
            The OCID of the user.
                :param UpdateUserDetails update_user_details: (required)
            Request object for updating a user.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type User
        """
        resource_path = "/users/{userId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
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

        :param str user_id: (required)
            The OCID of the user.
                :param UpdateStateDetails update_state_details: (required)
            Request object for updating a user state.
        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.
        :return: A Response object with data of type User
        """
        resource_path = "/users/{userId}/state/"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_user_state got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_state_details,
            response_type="User")

    def upload_api_key(self, user_id, create_api_key_details, **kwargs):
        """
        UploadApiKey
        Uploads an API signing key for the specified user.
        Every user has permission to use this operation to upload a key for *their own user ID*. An
        administrator in your organization does not need to write a policy to give users this ability.
        To compare, administrators who have permission to the tenancy can use this operation to upload a
        key for any user, including themselves.
        **Important:** Even though you have permission to upload an API key, you might not yet
        have permission to do much else. If you try calling an operation unrelated to your own credential
        management (e.g., `ListUsers`, `LaunchInstance`) and receive an \"unauthorized\" error,
        check with an administrator to confirm which IAM Service group(s) you're in and what access
        you have. Also confirm you're working in the correct compartment.
        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using
        the object, first make sure its `lifecycleState` has changed to ACTIVE.

        :param str user_id: (required)
            The OCID of the user.
                :param CreateApiKeyDetails create_api_key_details: (required)
            Request object for uploading an API key for a user.
        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).
        :return: A Response object with data of type ApiKey
        """
        resource_path = "/users/{userId}/apiKeys/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "upload_api_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=create_api_key_details,
            response_type="ApiKey")
