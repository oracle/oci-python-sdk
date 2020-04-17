# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import tests.util
import oci
import io
import os
import pytest

from . import util


@pytest.fixture
def namespace(object_storage):
    return object_storage.get_namespace().data


@pytest.fixture
def names():
    return {
        "read-object": "reallyLargeFile.dat",
        "read-bucket": util.bucket_prefix() + "ReadOnlyTestBucket4",
        "write-object": "file_test",
        "write-bucket": tests.util.unique_name("test_python_streaming", ignore_vcr=True),
        "temp-file": tests.util.get_resource_directory() + "/file_download_test_temp_file.dat"
    }


@pytest.yield_fixture
def write_bucket(namespace, object_storage, config, names):
    request = oci.object_storage.models.CreateBucketDetails()
    request.name = names["write-bucket"]
    request.compartment_id = config["tenancy"]
    response = object_storage.create_bucket(namespace, request)
    assert response.status == 200

    bucket = response.data

    yield bucket

    # Delete new objects and bucket
    try:
        object_list = object_storage.list_objects(namespace, bucket.name).data

        for summary in object_list.objects:
            response = object_storage.delete_object(namespace, bucket.name, summary.name)
            assert response.status == 204
    except Exception as e:
        print('TearDown: Could not delete new object. Error: {}'.format(str(e)))

    try:
        object_storage.delete_bucket(namespace, bucket.name)
    except Exception as e:
        print('TearDown: Could not delete new bucket. Error: {}'.format(str(e)))

    try:
        os.remove(names["temp-file"])
    except Exception as e:
        print('TearDown: Could not delete temporary local file. Error: {}'.format(str(e)))


def test_large_file_transfer(namespace, object_storage, write_bucket, names):
    """Download, upload, and delete a large file."""
    response = object_storage.head_object(
        namespace,
        names["read-bucket"],
        names["read-object"]
    )
    assert response.status == 200

    content_length = int(response.headers['content-length'])
    print('Downloading file with %s bytes....' % str(content_length))
    next_percent_to_report = 0
    chunk_count = 0
    total_size = 0
    chunk_size = 512
    initial_max_memory_usage = tests.util.max_memory_usage()
    print("Initial memory usage: {} bytes".format(str(initial_max_memory_usage)))

    with tests.util.timer('get large file'):
        response = object_storage.get_object(
            namespace,
            names["read-bucket"],
            names["read-object"]
        )
        assert response.status == 200
        with io.open(names["temp-file"], 'wb') as file:
            for chunk in response.data.iter_content(chunk_size=chunk_size):
                if len(chunk) < chunk_size:
                    print("Recieved {}, expected {}".format(len(chunk), chunk_size))
                total_size += len(chunk)
                chunk_count += 1
                file.write(chunk)
                percent = total_size * 100 / content_length
                if percent > next_percent_to_report:
                    print('%.0f percent complete' % percent)
                    next_percent_to_report += 2

                    # Make sure that memory usage doesn't go too far past where we started.
                    assert tests.util.max_memory_usage() < 3 * initial_max_memory_usage

        print('Download complete')

    print("Chunk count: {}".format(chunk_count))
    file_size = os.path.getsize(names["temp-file"])
    print("File size: {}".format(file_size))
    print("Total size: {}".format(total_size))
    assert chunk_count >= (total_size / chunk_size)
    assert total_size == int(response.headers['content-length'])
    assert total_size == file_size

    upload_msg = 'Uploading to bucket {} with name {}....'
    print(upload_msg.format(names["write-bucket"], names["write-object"]))
    with tests.util.timer('put large file'):
        with io.open(names["temp-file"], 'rb') as file:
            response = object_storage.put_object(
                namespace,
                names["write-bucket"],
                names["write-object"],
                file
            )
            assert response.status == 200

    response = object_storage.head_object(
        namespace,
        names["write-bucket"],
        names["write-object"]
    )
    assert response.status == 200

    uploaded_content_length = int(response.headers['content-length'])
    assert uploaded_content_length == file_size

    max_memory = tests.util.max_memory_usage() - initial_max_memory_usage
    print("Final max memory usage: {} bytes".format(str(max_memory)))
    assert max_memory < file_size
