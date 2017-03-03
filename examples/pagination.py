# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved.

import oraclebmc


config = oraclebmc.config.from_file()
compartment_id = config["tenancy"]
identity = oraclebmc.identity.IdentityClient(config)


# operation-independent pagination function
def paginate(operation, *args, **kwargs):
    """Yields values from a list call, automatically following pagination tokens.

    Metadata such as request_id, headers, and http status are not returned.
    :param operation: a client list function such as identity.list_policies
    """
    while True:
        response = operation(*args, **kwargs)
        for value in response.data:
            yield value
        kwargs["page"] = response.next_page
        if not response.has_next_page:
            break


for user in paginate(
        identity.list_users,
        compartment_id=compartment_id):
    print("User: " + str(user))


for group in paginate(
        identity.list_groups,
        compartment_id=compartment_id):
    print("Group: " + str(group))
