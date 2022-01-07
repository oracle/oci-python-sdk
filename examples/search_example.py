# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This example demonstrates how to programatically retrieve resource types and
# query for resources.
#
# The search service documentation can be found here:
# https://docs.cloud.oracle.com/iaas/Content/Search/Concepts/queryoverview.htm
#
# When running this example, it is assumed that you already have active users
# resources associated with your tenant to display the search results.
#
# Querying for resources may be done via a structured query or free text.
# For more information on how to format queries, please refer to
# https://docs.cloud.oracle.com/iaas/Content/Search/Concepts/querysyntax.htm

from __future__ import print_function
import oci


# Load the default configuration
config = oci.config.from_file()

# This is the root compartment.  You can use another compartment in your tenancy.
compartment_id = config["tenancy"]

search_client = oci.resource_search.ResourceSearchClient(config)


def resource_types():
    # Resource types
    # This is will produce a printed list of the resource types and fields
    # There are more details available than what is displayed.
    print()
    print("Resources and their fields")
    print("==========================")
    response = search_client.list_resource_types()
    for resource_type in response.data:
        print(resource_type.name)
        for field in resource_type.fields:
            print("\t {}".format(field.field_name))


def fields_in_instance_resource():
    # A more detailed look at the freeformTags field in the Instance resource
    print()
    print("Instance resource, freeformTags field")
    print("=====================================")
    response = search_client.list_resource_types()
    for resource_type in response.data:
        if resource_type.name == "Instance":
            instance = resource_type
            for field in instance.fields:
                print(field)


def field_names_in_instance_resource():
    # The details for a single resource type can be retrieved without
    # retrieving all the resources.
    print()
    print("Get a single resource type (Instance) from Search service")
    print("=========================================================")
    instance = search_client.get_resource_type('Instance').data
    fields = [x.field_name for x in instance.fields]
    print(fields)


def active_users():
    # Get all users which do not have the inactiveStatus set.
    # This is the same as "query user resources where lifecycleState = 'ACTIVE'"
    print()
    print("Get users which are active, using StructuredSearchDetails")
    print("=========================================================")
    structured_search = oci.resource_search.models.StructuredSearchDetails(query="query user resources where inactiveStatus = 0",
                                                                           type='Structured',
                                                                           matching_context_type=oci.resource_search.models.SearchDetails.MATCHING_CONTEXT_TYPE_NONE)
    users = search_client.search_resources(structured_search)

    for user in users.data.items:
        print(user.display_name)


def search_with_free_text():
    # Get all resources whose lifecycleState is AVAILABLE
    # Using pagination
    print("Get resources which are available, using FreeTextSearchDetails")
    print("==============================================================")

    free_text_search = oci.resource_search.models.FreeTextSearchDetails(text="lifecycleState as AVAILABLE",
                                                                        type='FreeText',
                                                                        matching_context_type=oci.resource_search.models.SearchDetails.MATCHING_CONTEXT_TYPE_HIGHLIGHTS)

    for response in oci.pagination.list_call_get_all_results_generator(search_client.search_resources, 'response', free_text_search):
        for resource in response.data.items:
            print("Resource type: {}, Resource name: {}".format(resource.resource_type, resource.display_name))


def users_by_freeformTag(tag):
    # Search for user resources with a freeform tag.
    print()
    print("Get users based on having a freeformTag")
    print("=======================================")
    structured_search = oci.resource_search.models.StructuredSearchDetails(query="query user resources where freeformTags.key = '{}'".format(tag),
                                                                           type='Structured',
                                                                           matching_context_type=oci.resource_search.models.SearchDetails.MATCHING_CONTEXT_TYPE_NONE)
    users = search_client.search_resources(structured_search)

    for user in users.data.items:
        print(user)


def users_by_freeformTag_and_value(tag, value):
    # Search for users with a freeform tag set to a particular value.
    print()
    print("Get users based on having a freeformTag which matches a value")
    print("=============================================================")
    structured_search = oci.resource_search.models.StructuredSearchDetails(query="query user resources where (freeformTags.key = '{}' && freeformTags.value = '{}')".format(tag, value),
                                                                           type='Structured',
                                                                           matching_context_type=oci.resource_search.models.SearchDetails.MATCHING_CONTEXT_TYPE_NONE)
    users = search_client.search_resources(structured_search)

    for user in users.data.items:
        print(user)


# Run examples
resource_types()
fields_in_instance_resource()
field_names_in_instance_resource()
search_with_free_text()
active_users()

# These next examples need to be customized to your situation.
# Let's assume you added a freeform tag "role" to some of your users and
# one of the values is "developer".  Then you could replace the
# <your_tag_here> with role and <your_value_here> with developer.
# These examples will then retrieve every user that had the role freeform tag
# and the role freeform tag where the value is set to developer.
# users_by_freeformTag("<your_tag_here>")
# users_by_freeformTag_and_value("<your_tag_here>", "<your_value_here>")
