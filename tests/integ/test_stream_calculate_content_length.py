# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

try:
    import unittest.mock as mock
except ImportError:
    import mock

import oci
import pytest
from tests.util import unique_name
from . import util
import os
import io
import tests.util
from oci.object_storage.transfer.constants import STREAMING_DEFAULT_PART_SIZE


@pytest.fixture
def namespace(object_storage):
    return object_storage.get_namespace().data


@pytest.yield_fixture
def bucket(object_storage, namespace, request):
    bucket_name = unique_name(request.node.name)
    request = oci.object_storage.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = util.COMPARTMENT_ID
    try:
        response = object_storage.create_bucket(namespace, request)
    except oci.exceptions.ServiceError as e:
        if e.status == 409 and e.code == 'BucketAlreadyExists':
            pass
        else:
            assert response.status == 200

    yield bucket_name

    for obj in object_storage.list_objects(namespace, bucket_name).data.objects:
        object_storage.delete_object(namespace, bucket_name, obj.name)
    response = object_storage.delete_bucket(namespace, bucket_name)
    assert response.status == 204


class FileLikeBody:
    def __init__(self,
                 no_read=None,
                 no_seek=None,
                 bad_seek=None,
                 no_tell=None,
                 bad_tell=None):
        if not no_read:
            self.read = mock.Mock()

        if not no_seek:
            if bad_seek:
                mock_seek = mock.Mock()
                mock_seek.side_effect = IOError
                self.seek = mock_seek
            else:
                mock_seek = mock.Mock()
                self.seek = mock_seek

        if not no_tell:
            if bad_tell:
                mock_tell = mock.Mock()
                mock_tell.side_effect = OSError
                self.tell = mock_tell
            else:
                mock_tell = mock.Mock()
                mock_tell.return_value = 5
                self.tell = mock_tell


class WrapperStream():
    def __init__(self,
                 file):
        self.file = file

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def read(self, n=10000):
        return self.file.read(n)


def test_failed_with_no_read_property(object_storage, namespace, bucket):
    stream_obj = FileLikeBody(no_read=True, no_tell=True)
    object_name = "object_with_no_read_property"
    with pytest.raises(TypeError):
        object_storage.put_object(namespace, bucket, object_name, stream_obj)


def test_failed_with_small_buffer_limit(object_storage, namespace, bucket):
    object_name = "object_with_no_file_no"
    test_file = tests.util.get_resource_path('test_image.png')
    object_name = 'large_file'
    with pytest.raises(BufferError):
        with open(test_file, 'rb') as file:
            stream_obj = WrapperStream(file)
            object_storage.put_object(namespace, bucket, object_name, stream_obj, buffer_limit=1)


def test_success_with_big_buffer_limit(object_storage, namespace, bucket):
    test_file = tests.util.get_resource_path('test_image.png')
    object_name = 'image_file'
    with open(test_file, 'rb') as file:
        verify_content_length = os.fstat(file.fileno()).st_size
        stream_obj = WrapperStream(file)
        res = object_storage.put_object(namespace, bucket, object_name, stream_obj, buffer_limit=STREAMING_DEFAULT_PART_SIZE)
        calculated_content_length = int(res.request.header_params['Content-Length'])
        assert calculated_content_length == verify_content_length
        object_storage.delete_object(namespace, bucket, object_name)


def test_success_file_with_no_fileno(object_storage, namespace, bucket):
    object_name = "object_with_no_fileno"
    large_file_path = os.path.join('tests', 'resources', 'large_file.bin')
    util.create_large_file(large_file_path, 1)  # Make a 1 MiB file
    with open(large_file_path, 'rb') as file:
        # Wrap it in a WrapperStream so the file contains no fileno property
        verify_content_length = os.fstat(file.fileno()).st_size
        stream_obj = WrapperStream(file)
        res = object_storage.put_object(namespace, bucket, object_name, stream_obj)
        calculated_content_length = int(res.request.header_params['Content-Length'])
        assert calculated_content_length == verify_content_length
        object_storage.delete_object(namespace, bucket, object_name)
    os.remove(large_file_path)


def test_code_path_should_not_call_back_up_body_calculate_stream_content_length(object_storage, namespace, bucket):
    object_name = "object_with_fileno"
    test_file = tests.util.get_resource_path('test_image.png')
    with open(test_file, 'rb') as file:
        verify_content_length = os.fstat(file.fileno()).st_size
        # small buffer_limit does not matter if code path does not take call_back_up_body_calculate_stream_content_length()
        object_storage.put_object(namespace, bucket, object_name, file, buffer_limit=1)
        response = object_storage.get_object(namespace, bucket, object_name)
        calculated_content_length = int(response.headers['Content-Length'])
        assert verify_content_length == calculated_content_length
        object_storage.delete_object(namespace, bucket, object_name)
