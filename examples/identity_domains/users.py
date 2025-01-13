# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script demonstrates how to list, search and get users in an identity domains tenancy, as well as the CRUD procedures.

import oci

# DEFAULT profile will load by default
# To use a different profile in ~/.oci/config:
# config = oci.config.from_file(profile_name='<replace with profile name>')
config = oci.config.from_file()
compartment_id = config["tenancy"]

# ATTN: regarding adding "domain_endpoint":
# To find Domain URL, naviage to Identity > Domains in OCI console, choose relevant domain,
# then in the overview page, find "Domain URL" under "Domain Information", click "Copy",
# open ~/.oci/config in editor of your choice, create custom value "domain_endpoint", paste the URL after the value name.
# Should look like: domain_endpoint=https://idcs-...
# Further reading: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains
# OCI config docs: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm

try:
    domain_url = config["domain_endpoint"]
except NameError:
    print("Please add \"domain_endpoint\" to your ~/.oci/config: view comments in the source code for more information.\n")

identity_domains_client = oci.identity_domains.IdentityDomainsClient(
    config=config, service_endpoint=domain_url
)

# List all users
user_list = identity_domains_client.list_users().data
print("Number of users: ", user_list.total_results)

# Get user
print("Printing first user details")
for user in user_list.resources:
    user1 = identity_domains_client.get_user(
        user_id=user.ocid, attribute_sets=["all"]
    ).data
    print(user1)
    break

# Create user
user_email = "pythonsdkexample@oracle.com"
print("Creating user with user_email ", user_email, "  ")
user = identity_domains_client.create_user(
    user=oci.identity_domains.models.User(
        name=oci.identity_domains.models.UserName(
            given_name="Python", family_name="Example"
        ),
        emails=[
            oci.identity_domains.models.UserEmails(
                value=user_email, type="work", primary=True
            ),
            oci.identity_domains.models.UserEmails(value="pythonsdkexample2@oracle.com", type="home"),
        ],
        user_name="python-sdk-example-user",
        display_name="Python SDK Example",
        schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
    )
).data
print(
    "Created user: ",
    user.ocid,
)

# Search for users using post
print("Searching for users with work email ", user_email, "  ")
user_search = identity_domains_client.search_users(
    user_search_request=oci.identity_domains.models.UserSearchRequest(
        schemas=["urn:ietf:params:scim:api:messages:2.0:SearchRequest"],
        filter='emails.value eq "' + user_email + '"',
    )
).data
returned_user_ocid = user_search.resources[0].ocid
print("Number of users with the email address = ", user_search.total_results)
print("Returned user matches with created user: ", (user.ocid == returned_user_ocid))

# Update user (patch)
print("Updating user's family name with PATCH")
user = identity_domains_client.patch_user(
    user_id=user.ocid,
    patch_op=oci.identity_domains.models.PatchOp(
        schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        operations=[
            {
                "op": "replace",
                "path": "name",
                "value": oci.identity_domains.models.UserName(
                    given_name="Python", family_name="SDK"
                ),
            }
        ],
    ),
).data
print("User new family name: ", user.name)

# Replace a user (put)
print("Replacing user with put")
user = identity_domains_client.put_user(
    user_id=user.ocid,
    user=oci.identity_domains.models.User(
        name=oci.identity_domains.models.UserName(
            given_name="PythonReplaced", family_name="ExampleReplaced"
        ),
        emails=[
            oci.identity_domains.models.UserEmails(
                value="1" + user_email, type="work", primary=True
            )
        ],
        user_name="python-sdk-example-user-replaced",
        display_name="Python SDK Example Replaced",
        schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
    ),
).data
print(
    "Replaced user username ",
    user.user_name,
    " with email ",
    user.emails[0].value,
    ", name ",
    user.name,
)

# Create a new Auth Token for the user
print("Creating auth token for the user")
auth_token = identity_domains_client.create_auth_token(
    auth_token=oci.identity_domains.models.AuthToken(
        description="new token",
        schemas=["urn:ietf:params:scim:schemas:oracle:idcs:authToken"],
        user=oci.identity_domains.models.AuthTokenUser(ocid=user.ocid),
    )
).data
print("Created auth token : ", auth_token)

# Update the Auth Token Description
print("Updating auth token with PATCH")
auth_token = identity_domains_client.patch_auth_token(
    auth_token_id=auth_token.ocid,
    patch_op=oci.identity_domains.models.PatchOp(
        schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        operations=[
            {"op": "replace", "path": "description", "value": "new token description"}
        ],
    ),
).data
print("Updated auth token description: ", auth_token.description)

# Delete the Auth Token
print("Deleting the auth token")
identity_domains_client.delete_auth_token(auth_token_id=auth_token.ocid)

# Create a customer secret key for the user
print("Creating a customer secret key for the user")
customer_secret = identity_domains_client.create_customer_secret_key(
    customer_secret_key=oci.identity_domains.models.CustomerSecretKey(
        description="new customer secret key",
        schemas=["urn:ietf:params:scim:schemas:oracle:idcs:customerSecretKey"],
        user=oci.identity_domains.models.CustomerSecretKeyUser(ocid=user.ocid),
    )
).data
print("Created customer secret key: ", customer_secret)

# Patch the customer secret key
print("Updating the customer secret key with PATCH")
customer_secret = identity_domains_client.patch_customer_secret_key(
    customer_secret_key_id=customer_secret.ocid,
    patch_op=oci.identity_domains.models.PatchOp(
        schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        operations=[
            {
                "op": "replace",
                "path": "description",
                "value": "updated customer secret key description",
            }
        ],
    ),
).data
print("Updated customer secret key description: ", customer_secret.description)

# Delete the customer secret key
print("Deleting the customer secret key")
identity_domains_client.delete_customer_secret_key(
    customer_secret_key_id=customer_secret.ocid
)

# GROUPS & GROUP MEMBERSHIP

# Create a new group
print("Creating a new group")
group_name = "SDK Example Test Group"
group = identity_domains_client.create_group(
    group=oci.identity_domains.models.Group(
        display_name=group_name, schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"]
    )
).data
print("Created group: ", group.ocid)

# Add the new user to the newly created group
print("Adding user to the new group")
group = identity_domains_client.patch_group(
    group_id=group.ocid,
    patch_op=oci.identity_domains.models.PatchOp(
        schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        operations=[
            {
                "op": "add",
                "path": "members",
                "value": [{"value": user.id, "type": "User"}],
            }
        ],
    ),
).data

# Verify if user is added to the group
print("Verifying if user is added to the group")
group_users = identity_domains_client.get_group(
    group_id=group.ocid,
    attributes='members[type eq "User" and value eq "' + user.id + '"]',
).data
for m in group_users.members:
    if user.ocid == m.ocid:
        print("user is in the group")
        break

# Remove the user from the group
print("Removing user from the group")
identity_domains_client.patch_group(
    group_id=group.ocid,
    patch_op=oci.identity_domains.models.PatchOp(
        schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        operations=[
            {
                "op": "remove",
                "path": "members",
                "value": [{"value": user.id, "type": "User"}],
            }
        ],
    ),
)

# Delete the group
print("Deleting group ", group.ocid, "  ")
identity_domains_client.delete_group(group_id=group.ocid)

# Delete user
print("Deleting user ", user.ocid, "  ")
identity_domains_client.delete_user(user_id=user.ocid)
