# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use archive storage in the Object Storage service. This example
# will create an archive storage bucket and demonstrate putting and restoring objects.
# This script accepts two arguments:
#
#   * The first argument is the OCID of the compartment where we'll create a bucket
#   * The second is the name of bucket to create

import oci
import sys


if len(sys.argv) != 3:
    raise RuntimeError('This script expects an argument of a compartment OCID where the bucket will be created, and the name of the bucket')

# The first argument is the name of the script, so start the index at 1
compartment_id = sys.argv[1]
bucket_name = sys.argv[2]

# Default config file and profile
config = oci.config.from_file()
object_storage_client = oci.object_storage.ObjectStorageClient(config)

namespace = object_storage_client.get_namespace().data

create_bucket_response = object_storage_client.create_bucket(
    namespace,
    oci.object_storage.models.CreateBucketDetails(
        name=bucket_name,
        compartment_id=compartment_id,
        storage_tier='Archive',
        public_access_type='ObjectRead'
    )
)
print('Created archive storage bucket:\n{}'.format(create_bucket_response.data))
print('\n=========================\n')

# We use the same operation to put an object in a bucket, regardless of its storage tier. Note that the response
# does not contain a body but the headers will contain information about the object, such as its ETag and MD5
object_name = 'archive_object_test'
put_object_response = object_storage_client.put_object(namespace, bucket_name, object_name, 'Test object content')
print('Put object into archive storage bucket:\n{}'.format(create_bucket_response.headers))
print('\n=========================\n')

# If an object is archived, then we cannot do a get_object. This will throw an exception with a HTTP 409 status
# and a code of NotRestored
try:
    object_storage_client.get_object(namespace, bucket_name, object_name)
except oci.exceptions.ServiceError as e:
    print('Attempt to get archived object:\n{}'.format(e))
    print('\n=========================\n')


# We can, however, HEAD the object to get its current status. The response will not have a body, but the headers
# will contain information. One key header of interest is archival-state. In this case, because we have only
# put the object in the bucket, it will start out as "Archived".
#
# See https://docs.cloud.oracle.com/api/#/en/objectstorage/20160918/Object/HeadObject for
# more information on available headers
head_object_response = object_storage_client.head_object(namespace, bucket_name, object_name)
print('Archive state from head_object: {}'.format(head_object_response.headers['archival-state']))
print('All headers:\n{}'.format(head_object_response.headers))
print('\n=========================\n')


# We can restore an object in archive storage (so that the GetObject will work) by using the restore_objects
# operation. In RestoreObjectsDetails, the hours field represents how long after restoration has completed that
# the object will be available for before being archived again. If no value is specified,
# this will default to 24 hours
object_storage_client.restore_objects(
    namespace,
    bucket_name,
    oci.object_storage.models.RestoreObjectsDetails(
        object_name=object_name,
        hours=72
    )
)

# Objects take some time to restore. During that time get_object will still throw an exception
# with a HTTP 409 status and a code of NotRestored
try:
    object_storage_client.get_object(namespace, bucket_name, object_name)
except oci.exceptions.ServiceError as e:
    print('Attempt to get a restoring object:\n{}'.format(e))
    print('\n=========================\n')

# We can use head_object to check/poll the status of the object. The headers of interest are archival-state
# and time-of-archival. While the object is restoring, archival-state will be "Restoring" and when
# it is "Restored" then a get_object can be done successfully.
#
# For a restored object, the time-of-archival will be when the object will be archived again.
#
# See https://docs.cloud.oracle.com/api/#/en/objectstorage/20160918/Object/HeadObject for
# more information on available headers
head_object_response = object_storage_client.head_object(namespace, bucket_name, object_name)
print('Archive state from head_object: {}'.format(head_object_response.headers['archival-state']))
print('All headers:\n{}'.format(head_object_response.headers))
print('\n=========================\n')

# Clean up
object_storage_client.delete_object(namespace, bucket_name, object_name)
print('Deleted object')

object_storage_client.delete_bucket(namespace, bucket_name)
print('Deleted bucket')
