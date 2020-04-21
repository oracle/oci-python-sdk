# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import filecmp
import oci
from oci.object_storage.models import CreateBucketDetails


config = oci.config.from_file()
compartment_id = config["tenancy"]
object_storage = oci.object_storage.ObjectStorageClient(config)

namespace = object_storage.get_namespace().data
bucket_name = "python-sdk-example-bucket"
object_name = "python-sdk-example-object"
my_data = b"Hello, World!"

print("Creating a new bucket {!r} in compartment {!r}".format(
    bucket_name, compartment_id))
request = CreateBucketDetails()
request.compartment_id = compartment_id
request.name = bucket_name
bucket = object_storage.create_bucket(namespace, request)

print("Uploading new object {!r}".format(object_name))
obj = object_storage.put_object(
    namespace,
    bucket_name,
    object_name,
    my_data)

same_obj = object_storage.get_object(
    namespace,
    bucket_name,
    object_name)

print("{!r} == {!r}: {}".format(
    my_data, same_obj.data.content,
    my_data == same_obj.data.content))

print('Uploading a file to object storage')

# First create a sample file
sample_content = b'a' * 1024 * 1024 * 5
with open('example_file', 'wb') as f:
    f.write(sample_content)

# Then upload the file to Object Storage
example_file_object_name = 'example_file_obj'
with open('example_file', 'rb') as f:
    obj = object_storage.put_object(namespace, bucket_name, example_file_object_name, f)

# Retrieve the file, streaming it into another file in 1 MiB chunks
print('Retrieving file from object storage')
get_obj = object_storage.get_object(namespace, bucket_name, example_file_object_name)
with open('example_file_retrieved', 'wb') as f:
    for chunk in get_obj.data.raw.stream(1024 * 1024, decode_content=False):
        f.write(chunk)

print('Uploaded and downloaded files are the same: {}'.format(filecmp.cmp('example_file', 'example_file_retrieved')))

print("Deleting object {}".format(object_name))
object_storage.delete_object(namespace, bucket_name, object_name)

print("Deleting object {}".format(example_file_object_name))
object_storage.delete_object(namespace, bucket_name, example_file_object_name)

print("Deleting bucket {}".format(bucket_name))
object_storage.delete_bucket(namespace, bucket_name)
