# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import oraclebmc
from oraclebmc.identity.models import AddUserToGroupDetails, CreateGroupDetails, CreateUserDetails

# Default config file and profile
config = oraclebmc.config.from_file()
compartment_id = config["tenancy"]
# Service client
identity = oraclebmc.identity.IdentityClient(config)


user_name = "python-sdk-example-user"
group_name = "python-sdk-example-group"


print("Creating a new user {!r} in compartment {!r}".format(
    user_name, compartment_id))

request = CreateUserDetails()
request.compartment_id = compartment_id
request.name = user_name
request.description = "Created by a Python SDK example"
user = identity.create_user(request)
print(user.data)


print("Creating a new group {!r} in compartment {!r}".format(
    group_name, compartment_id))

request = CreateGroupDetails()
request.compartment_id = compartment_id
request.name = group_name
request.description = "Created by a Python SDK example"
group = identity.create_group(request)
print(group.data)

print("Adding new user to the new group")
request = AddUserToGroupDetails()
request.user_id = user.data.id
request.group_id = group.data.id
membership = identity.add_user_to_group(request)
print(membership.data)

print("Cleaning up resources.")
print("Removing {!r} from {!r}.".format(
    user_name, group_name))
identity.remove_user_from_group(membership.data.id)

print("Deleting user {!r}".format(user_name))
identity.delete_user(user.data.id)

print("Deleting group {!r}".format(group_name))
identity.delete_group(group.data.id)
