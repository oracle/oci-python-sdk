# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides an example on how to use tagging in the Python SDK to manage tags and tag namespaces, as
# well as how to apply freeform and defined tags to a resource.

import oci
import random
import time

# Default config file and profile
config = oci.config.from_file()
compartment_id = '<Your compartment OCID here>'

identity = oci.identity.IdentityClient(config)

# Create a namespace
example_namespace_name = 'examplens_{}'.format(random.randint(0, 1000000))
create_tag_namespace_response = identity.create_tag_namespace(
    oci.identity.models.CreateTagNamespaceDetails(
        compartment_id=compartment_id,
        name=example_namespace_name,
        description='Python SDK example tag namespace'
    )
)
tag_namespace_id = create_tag_namespace_response.data.id
print('Created tag namespace: {}'.format(create_tag_namespace_response.data))

# Create a tag
tag_one_name = 'tagone_{}'.format(random.randint(0, 1000000))
create_tag_one_response = identity.create_tag(
    tag_namespace_id,
    oci.identity.models.CreateTagDetails(
        name=tag_one_name,
        description='Python SDK example tag one'
    )
)
print('Created tag: {}'.format(create_tag_one_response.data))

# Create another tag
tag_two_name = 'tagtwo_{}'.format(random.randint(0, 1000000))
create_tag_two_response = identity.create_tag(
    tag_namespace_id,
    oci.identity.models.CreateTagDetails(
        name=tag_two_name,
        description='Python SDK example tag two'
    )
)
print('Created tag: {}'.format(create_tag_one_response.data))

# We can retire a tag by using the update tag operation
update_tag_one_response = identity.update_tag(
    tag_namespace_id,
    tag_one_name,
    oci.identity.models.UpdateTagDetails(is_retired=True)
)
print('Updated tag (retired): {}'.format(update_tag_one_response.data))

# We can retrieve individual tags and namespaces
tag_namespace = identity.get_tag_namespace(tag_namespace_id).data
tag_one = identity.get_tag(tag_namespace_id, tag_one_name).data
tag_two = identity.get_tag(tag_namespace_id, tag_two_name).data

# We can list tags and namespaces. These operations are paginated and take a "page" parameter to allow you
# to get the next batch of items from the server
tag_namespaces = identity.list_tag_namespaces(compartment_id).data
tags_in_namespace = identity.list_tags(tag_namespace.id).data

# We can also reactivate a tag using the update tag operation
update_tag_one_response = identity.update_tag(
    tag_namespace_id,
    tag_one_name,
    oci.identity.models.UpdateTagDetails(is_retired=False)
)
print('Updated tag (reactivated): {}'.format(update_tag_one_response.data))

virtual_network = oci.core.VirtualNetworkClient(config)

# We can assign freeform and defined tags at creation time. Freeform tags are a dictionary of string-to-string,
# where the key is the tag name and the value is the tag value.
#
# Defined tags are a dictionary where the key is the tag namespace (string) and the value is another dictionary. In
# this second dictionary, the key is the tag name (string) and the value is the tag value. The tag names have to
# correspond to the name of a tag within the specified namespace (and the namespace must exist).
#
# Resources where we can create/update tags will have the freeform_tags and defined_tags attributes. Consult the API
# documentation to see what these are (https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/landing.html)
num_tries = 0
while True:
    # You may get a 400 if you create/reactivate a tag and try and use it straight away. If you have a delay/sleep between
    # creating the tag and then using it (or alternatively retry the 400) that may resolve the issue.
    try:
        create_vcn_response = virtual_network.create_vcn(
            oci.core.models.CreateVcnDetails(
                cidr_block='10.0.0.0/16',
                compartment_id=compartment_id,
                display_name='Python SDK tagging example VCN',
                dns_label='vcn{}'.format(random.randint(0, 1000000)),
                freeform_tags={'free': 'form', 'another': 'item'},
                defined_tags={tag_namespace.name: {tag_one_name: 'hello', tag_two_name: 'world'}}
            )
        )
        vcn_id = create_vcn_response.data.id
        vcn_after_wait_response = oci.wait_until(virtual_network, virtual_network.get_vcn(vcn_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)
        print('Created VCN with tags: {}'.format(vcn_after_wait_response.data))
        break
    except oci.exceptions.ServiceError as e:
        if e.status == 400:
            print('Retrying on 400: {}'.format(e))
            num_tries += 1
            if num_tries >= 3:  # If we can't get it in 3 tries, something else may be going on
                raise
            else:
                time.sleep(5)
        else:
            raise

# We can also update tags on a resource. Note that this is a total replacement for any previously set freeform or defined tags.
#
# Resources where we can create/update tags will have the freeform_tags and defined_tags attributes. Consult the API
# documentation to see what these are (https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/landing.html)
update_vcn_response = virtual_network.update_vcn(
    vcn_id,
    oci.core.models.UpdateVcnDetails(
        freeform_tags={'total': 'replace'},
        defined_tags={tag_namespace.name: {tag_two_name: 'also replaced'}}
    )
)
print('Updated tags on VCN: {}'.format(update_vcn_response.data))

# We can also totally remove tags on a resource by passing in an empty dictionary for those tagging parameters
update_vcn_response = virtual_network.update_vcn(
    vcn_id,
    oci.core.models.UpdateVcnDetails(
        freeform_tags={},
        defined_tags={}
    )
)
print('Removed tags from VCN: {}'.format(update_vcn_response.data))

# Previously we saw retiring a tag. We can also retire a tag namespace - this will also retire any tags in that namespace
update_tag_namespace_response = identity.update_tag_namespace(
    tag_namespace.id,
    oci.identity.models.UpdateTagNamespaceDetails(is_retired=True)
)
print('Updated tag namespace (retired): {}'.format(update_tag_namespace_response.data))
print('Tags in namespace: {}'.format(identity.list_tags(tag_namespace.id).data))

# We can also reactivate a namespace. Note that this doesn't reactivate the tags in that namespace - those tags will need
# to be reactivated individually
update_tag_namespace_response = identity.update_tag_namespace(
    tag_namespace.id,
    oci.identity.models.UpdateTagNamespaceDetails(is_retired=False)
)
print('Updated tag namespace (reactivated): {}'.format(update_tag_namespace_response.data))
print('Tags in namespace: {}'.format(identity.list_tags(tag_namespace.id).data))

identity.update_tag_namespace(
    tag_namespace.id,
    oci.identity.models.UpdateTagNamespaceDetails(is_retired=True)
)
