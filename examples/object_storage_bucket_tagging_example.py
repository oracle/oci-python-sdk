# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to tag buckets in Object Storage.
# This script accepts four arguments:
#
#   * The first argument is the OCID of the compartment where we'll create a bucket
#   * The second is the name of bucket to create
#   * The third is the name (not OCID) of the tag namespace to use in defined tags
#   * The fourth is the name of a tag in the tag namespace to use defined tags

import oci
import sys

if len(sys.argv) != 5:
    raise RuntimeError('Unexpected number of arguments received. Consult the script header comments for expected arguments')

compartment_id = sys.argv[1]
bucket_name = sys.argv[2]
tag_namespace = sys.argv[3]
tag_name = sys.argv[4]

# Default config file and profile
config = oci.config.from_file()
object_storage_client = oci.object_storage.ObjectStorageClient(config)

namespace = object_storage_client.get_namespace().data

# We can assign tags to a bucket at creation time. Like other taggable resources, we can
# assign freeform and defined tags to a bucket.  Freeform tags are a dictionary of
# string-to-string, where the key is the tag name and the value is the tag value.
#
# Defined tags are a dictionary where the key is the tag namespace (string) and the value is another dictionary. In
# this second dictionary, the key is the tag name (string) and the value is the tag value. The tag names have to
# correspond to the name of a tag within the specified namespace (and the namespace must exist).
create_bucket_response = object_storage_client.create_bucket(
    namespace,
    oci.object_storage.models.CreateBucketDetails(
        name=bucket_name,
        compartment_id=compartment_id,
        public_access_type='ObjectRead',
        freeform_tags={'free': 'form', 'another': 'item'},
        defined_tags={tag_namespace: {tag_name: 'value at create'}}
    )
)
print('Created a bucket with tags:\n{}'.format(create_bucket_response.data))
print('\n=========================\n')

# Tags come back when retrieving the bucket
get_bucket_response = object_storage_client.get_bucket(namespace, bucket_name)
print('Retrieved bucket with tags:\n{}'.format(get_bucket_response.data))
print('\n=========================\n')

# Unlike other resources (e.g. instances, VCNs, and block volumes), when listing buckets
# tags are not returned by default. Instead, you need to provide a value to the fields
# parameter when listing buckets in order to have those tags returned.
#
# Here we can see the result of providing and not providing that parameter.
list_buckets_without_asking_for_tags_generator = oci.pagination.list_call_get_all_results_generator(
    object_storage_client.list_buckets,
    'record',
    namespace,
    compartment_id
)
for bucket in list_buckets_without_asking_for_tags_generator:
    if bucket.name == bucket_name:
        print('Bucket summary without tags:\n{}'.format(bucket))
        print('\n=========================\n')
        break

list_buckets_asking_for_tags_generator = oci.pagination.list_call_get_all_results_generator(
    object_storage_client.list_buckets,
    'record',
    namespace,
    compartment_id,
    fields=['tags']
)
for bucket in list_buckets_asking_for_tags_generator:
    if bucket.name == bucket_name:
        print('Bucket summary with tags:\n{}'.format(bucket))
        print('\n=========================\n')
        break

# We can also update tags on a bucket. Note that this is a total replacement for any
# previously set freeform or defined tags.
update_bucket_response = object_storage_client.update_bucket(
    namespace,
    bucket_name,
    oci.object_storage.models.UpdateBucketDetails(
        name=bucket_name,
        freeform_tags={'new': 'freeform'},
        defined_tags={tag_namespace: {tag_name: 'replaced'}}
    )
)
print('Updated a bucket with new tags:\n{}'.format(update_bucket_response.data))
print('\n=========================\n')

# We can also clear tags from a bucket by passing empty dicts to the tag parameters
update_bucket_response = object_storage_client.update_bucket(
    namespace,
    bucket_name,
    oci.object_storage.models.UpdateBucketDetails(
        name=bucket_name,
        freeform_tags={},
        defined_tags={}
    )
)
print('Cleared tags on the bucket:\n{}'.format(update_bucket_response.data))
print('\n=========================\n')

# Clean up
object_storage_client.delete_bucket(namespace, bucket_name)
print('Deleted bucket')
