# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import pytest
from tests.util import unique_name
from . import util
import filecmp
import os
import io
from oci.object_storage.transfer.constants import MEBIBYTE


@pytest.fixture
def namespace(object_storage):
    return object_storage.get_namespace().data


@pytest.yield_fixture
def bucket(object_storage, namespace, request):
    bucket_name = unique_name(request.node.name, ignore_vcr=True)
    request = oci.object_storage.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = util.COMPARTMENT_ID
    response = object_storage.create_bucket(namespace, request)
    assert response.status == 200

    yield bucket_name

    # Clear pending multipart uploads
    pending_multipart_uploads = object_storage.list_multipart_uploads(namespace, bucket_name).data
    for pending_multipart_upload in pending_multipart_uploads:
        upload_id = pending_multipart_upload.upload_id
        object_name = pending_multipart_upload.object
        object_storage.abort_multipart_upload(namespace, bucket_name, object_name, upload_id)

    for obj in object_storage.list_objects(namespace, bucket_name).data.objects:
        object_storage.delete_object(namespace, bucket_name, obj.name)
    response = object_storage.delete_bucket(namespace, bucket_name)
    assert response.status == 204


# A utility class which intercepts response from service to inject ConnectTimeout on the first attempt
# It also counts the number of retrying attempts
class TestRetry:
    def __init__(self):
        self.attempts = 0

    def hack_response(self, response, *args, **kwargs):
        self.attempts += 1
        if self.attempts <= 1:
            # Raise ConnectionError for the first attempt
            raise oci.exceptions.ConnectTimeout
        # Do nothing for the second time, just return response
        return response


# A utility class which reads only 4 MiB of data in the first attempt, to simulate a case of request failing mid-request
# The TestRetry class raises Connect Timeout for the first attempt to force retries
class BadBody(io.IOBase):
    def __init__(self,
                 file):
        self.file = file
        self.attempts = 0

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def read(self, n=-1):
        if self.attempts < 1:
            self.attempts += 1
            # On the first attempt,read 4 MB and then raise an error to retry
            # TestRetry.hack_response will raise the error after first attempt
            return self.file.read(4 * MEBIBYTE)
        return self.file.read(n)


def test_bad_body():
    large_file_path = os.path.join('tests', 'resources', 'large_file.bin')
    util.create_large_file(large_file_path, 10)  # Make a 10 MiB file

    with open(large_file_path, 'rb') as f:
        bad_request_body = BadBody(f)

        # Read 4 MiB on attempt 1
        read_bytes = bad_request_body.read()
        assert len(read_bytes) / MEBIBYTE == 4.0

        # Read the rest 6 MiB on attempt 2
        read_bytes = bad_request_body.read()
        assert len(read_bytes) / MEBIBYTE == 6.0

    os.remove(large_file_path)


def test_put_object_with_retry_file(object_storage, namespace, bucket):
    test_retry = TestRetry()
    large_file_path = os.path.join('tests', 'resources', 'large_file.bin')
    util.create_large_file(large_file_path, 10)  # Make a 10 MiB file
    object_name = 'large_file'
    # The object storage client has retries enabled already

    # Add event hook to the session to raise ConnectTimeout and force retries
    object_storage.base_client.session.hooks['response'].append(test_retry.hack_response)
    with open(large_file_path, 'rb') as f:
        bad_request_body = BadBody(f)
        object_storage.put_object(namespace, bucket, object_name, bad_request_body)
    # Disable the hook
    object_storage.base_client.session.hooks['response'] = []

    # Check that the request was actually retried
    assert test_retry.attempts > 1

    # Download the file and compare
    response = object_storage.get_object(
        namespace_name=namespace,
        bucket_name=bucket,
        object_name=object_name
    )
    downloaded_large_file_path = os.path.join('tests', 'resources', 'downloaded_large_file.bin')
    with open(downloaded_large_file_path, 'wb') as file:
        for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
            file.write(chunk)

    assert filecmp.cmp(large_file_path, downloaded_large_file_path, shallow=False)

    # Clean up
    os.remove(downloaded_large_file_path)
    os.remove(large_file_path)
    object_storage.delete_object(namespace, bucket, object_name)


def empty_progess_callback(bytes_read):
    pass


def test_put_object_with_retry_multipart_disabled_with_callback(object_storage, namespace, bucket):
    test_retry = TestRetry()
    large_file_path = os.path.join('tests', 'resources', 'large_file.bin')
    util.create_large_file(large_file_path, 10)  # Make a 10 MiB file
    object_name = 'large_file'
    # The object storage client has retries enabled already

    # Add event hook to the session to raise ConnectTimeout and force retries
    object_storage.base_client.session.hooks['response'].append(test_retry.hack_response)
    part_size = 2 * MEBIBYTE  # part size (in bytes)
    upload_manager = oci.object_storage.UploadManager(object_storage, allow_multipart_uploads=False)
    upload_manager.upload_file(
        namespace, bucket, object_name, large_file_path, part_size=part_size, progress_callback=empty_progess_callback)

    # Disable the hook
    object_storage.base_client.session.hooks['response'] = []

    # Check that the request was actually retried
    assert test_retry.attempts > 1

    # Download the file and compare
    response = object_storage.get_object(
        namespace_name=namespace,
        bucket_name=bucket,
        object_name=object_name
    )
    downloaded_large_file_path = os.path.join('tests', 'resources', 'downloaded_large_file.bin')
    with open(downloaded_large_file_path, 'wb') as file:
        for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
            file.write(chunk)

    assert filecmp.cmp(large_file_path, downloaded_large_file_path, shallow=False)

    # Clean up
    os.remove(downloaded_large_file_path)
    os.remove(large_file_path)
    object_storage.delete_object(namespace, bucket, object_name)


def test_put_object_with_retry_multipart_disabled_without_callback(object_storage, namespace, bucket):
    test_retry = TestRetry()
    large_file_path = os.path.join('tests', 'resources', 'large_file.bin')
    util.create_large_file(large_file_path, 10)  # Make a 10 MiB file
    object_name = 'large_file'
    # The object storage client has retries enabled already

    # Add event hook to the session to raise ConnectTimeout and force retries
    object_storage.base_client.session.hooks['response'].append(test_retry.hack_response)
    part_size = 2 * MEBIBYTE  # part size (in bytes)
    upload_manager = oci.object_storage.UploadManager(object_storage, allow_multipart_uploads=False)
    upload_manager.upload_file(
        namespace, bucket, object_name, large_file_path, part_size=part_size)

    # Disable the hook
    object_storage.base_client.session.hooks['response'] = []

    # Check that the request was actually retried
    assert test_retry.attempts > 1

    # Download the file and compare
    response = object_storage.get_object(
        namespace_name=namespace,
        bucket_name=bucket,
        object_name=object_name
    )
    downloaded_large_file_path = os.path.join('tests', 'resources', 'downloaded_large_file.bin')
    with open(downloaded_large_file_path, 'wb') as file:
        for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
            file.write(chunk)

    assert filecmp.cmp(large_file_path, downloaded_large_file_path, shallow=False)

    # Clean up
    os.remove(downloaded_large_file_path)
    os.remove(large_file_path)
    object_storage.delete_object(namespace, bucket, object_name)


def test_put_object_with_retry_multipart(object_storage, namespace, bucket):
    test_retry = TestRetry()
    large_file_path = os.path.join('tests', 'resources', 'large_file.bin')
    util.create_large_file(large_file_path, 10)  # Make a 10 MiB file
    object_name = 'large_file'
    # The object storage client has retries enabled already

    # Add event hook to the session to raise ConnectTimeout and force retries
    object_storage.base_client.session.hooks['response'].append(test_retry.hack_response)
    part_size = 2 * MEBIBYTE  # part size (in bytes)
    upload_manager = oci.object_storage.UploadManager(object_storage, allow_parallel_uploads=True,
                                                      parallel_process_count=3)
    upload_manager.upload_file(
        namespace, bucket, object_name, large_file_path, part_size=part_size)

    # Disable the hook
    object_storage.base_client.session.hooks['response'] = []

    # Check that the request was actually retried
    assert test_retry.attempts > 1

    # Download the file and compare
    response = object_storage.get_object(
        namespace_name=namespace,
        bucket_name=bucket,
        object_name=object_name
    )
    downloaded_large_file_path = os.path.join('tests', 'resources', 'downloaded_large_file.bin')
    with open(downloaded_large_file_path, 'wb') as file:
        for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
            file.write(chunk)

    assert filecmp.cmp(large_file_path, downloaded_large_file_path, shallow=False)

    # Clean up
    os.remove(downloaded_large_file_path)
    os.remove(large_file_path)
    object_storage.delete_object(namespace, bucket, object_name)


def test_put_object_with_retry_multipart_single_thread(object_storage, namespace, bucket):
    test_retry = TestRetry()
    large_file_path = os.path.join('tests', 'resources', 'large_file.bin')
    util.create_large_file(large_file_path, 10)  # Make a 10 MiB file
    object_name = 'large_file'
    # The object storage client has retries enabled already

    # Add event hook to the session to raise ConnectTimeout and force retries
    object_storage.base_client.session.hooks['response'].append(test_retry.hack_response)
    part_size = 2 * MEBIBYTE  # part size (in bytes)
    upload_manager = oci.object_storage.UploadManager(object_storage, allow_parallel_uploads=False)
    upload_manager.upload_file(
        namespace, bucket, object_name, large_file_path, part_size=part_size)

    # Disable the hook
    object_storage.base_client.session.hooks['response'] = []

    # Check that the request was actually retried
    assert test_retry.attempts > 1

    # Download the file and compare
    response = object_storage.get_object(
        namespace_name=namespace,
        bucket_name=bucket,
        object_name=object_name
    )
    downloaded_large_file_path = os.path.join('tests', 'resources', 'downloaded_large_file.bin')
    with open(downloaded_large_file_path, 'wb') as file:
        for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
            file.write(chunk)

    assert filecmp.cmp(large_file_path, downloaded_large_file_path, shallow=False)

    # Clean up
    os.remove(downloaded_large_file_path)
    os.remove(large_file_path)
    object_storage.delete_object(namespace, bucket, object_name)


def test_put_object_with_retry_file_multipart_stream(object_storage, namespace, bucket):
    test_retry = TestRetry()
    b = b'0123456789abcdefg'
    data_size = 10 * MEBIBYTE
    data = (b * (data_size // len(b))) + (b'x' * (data_size % len(b)))
    assert len(data) == data_size
    object_name = 'large_stream'
    part_size = 2 * MEBIBYTE
    # Upload
    s = io.BytesIO(data)
    # The object storage client has retries enabled already
    upload_manager = oci.object_storage.UploadManager(
        object_storage,
        allow_parallel_uploads=True,
        parallel_process_count=3)
    # Add event hook to the session to raise ConnectTimeout and force retries
    object_storage.base_client.session.hooks['response'].append(test_retry.hack_response)
    upload_manager.upload_stream(
        namespace,
        bucket,
        object_name,
        s,
        part_size=part_size)
    # Disable the hook
    object_storage.base_client.session.hooks['response'] = []
    # Check that the request was actually retried
    assert test_retry.attempts > 1
    # Download
    get_result = object_storage.get_object(
        namespace_name=namespace,
        bucket_name=bucket,
        object_name=object_name)
    downloaded = bytearray(len(data))
    get_result.data.raw.readinto(downloaded)
    # Check if both objects are same
    assert data == downloaded

    object_storage.delete_object(namespace, bucket, object_name)
