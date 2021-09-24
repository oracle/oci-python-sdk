# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import filecmp
import io
import os
import os.path
import pytest
import resource
import subprocess
import sys
import time
import oci
from oci._vendor import six
from oci.object_storage.transfer.constants import MEBIBYTE
from oci.object_storage import MultipartObjectAssembler
from oci.object_storage import UploadManager
from tests.util import get_resource_path, unique_name
from . import util

LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES = 3


def delete_objects_in_bucket(object_storage, namespace, bucket_name):
    for obj in oci.pagination.list_call_get_all_results(object_storage.list_objects, namespace, bucket_name).data.objects:
        object_storage.delete_object(namespace, bucket_name, obj.name)


def create_bucket(object_storage, namespace, bucket_name):
    request = oci.object_storage.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = util.COMPARTMENT_ID
    response = object_storage.create_bucket(namespace, request)
    assert response.status == 200

    return response


@pytest.fixture(scope="class")
def namespace(object_storage):
    return object_storage.get_namespace().data


@pytest.fixture(scope='function')
def content_input_file():
    filename = 'tests/resources/multipart_content_input.txt'

    # generate large file for multipart testing
    util.create_large_file(filename, LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)

    yield filename

    if os.path.exists(filename):
        os.remove(filename)


@pytest.fixture
def non_vcr_bucket(object_storage, namespace, request):
    bucket_name = unique_name(request.node.name, ignore_vcr=True)
    response = create_bucket(object_storage, namespace, bucket_name)
    assert response.status == 200

    yield bucket_name

    delete_objects_in_bucket(object_storage, namespace, bucket_name)
    response = object_storage.delete_bucket(namespace, bucket_name)
    assert response.status == 204


class TestUploadManager:

    def test_upload_manager_single_part_based_on_file_size(self, object_storage, non_vcr_bucket, content_input_file):
        object_name = 'test_object_multipart'
        namespace = object_storage.get_namespace().data

        # explicitly use part-size > file size to trigger single part upload
        part_size_in_bytes = (LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES + 1) * MEBIBYTE
        upload_manager = oci.object_storage.UploadManager(object_storage, allow_multipart_uploads=True)
        response = upload_manager.upload_file(
            namespace, non_vcr_bucket, object_name, content_input_file, part_size=part_size_in_bytes)
        util.validate_response(response)

        # confirm that the object was actually uploaded with single part
        assert response.headers['opc-content-md5']

    def test_upload_manager_multipart_part_based_on_file_size(self, object_storage, non_vcr_bucket, content_input_file):
        object_name = 'test_object_multipart'
        namespace = object_storage.get_namespace().data

        # explicitly use part_size < file size to trigger multipart
        part_size_in_bytes = (LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES - 1) * MEBIBYTE
        upload_manager = oci.object_storage.UploadManager(object_storage, allow_multipart_uploads=True)
        response = upload_manager.upload_file(
            namespace, non_vcr_bucket, object_name, content_input_file, part_size=part_size_in_bytes)
        util.validate_response(response)

        # confirm that the object was actually uploaded with multipart
        assert response.headers['opc-multipart-md5']

        print('Downloading object {} from {} for verification'.format(object_name, non_vcr_bucket))
        response = object_storage.get_object(
            namespace_name=namespace,
            bucket_name=non_vcr_bucket,
            object_name=object_name
        )
        downloaded_file_path = os.path.join('tests', 'resources', 'downloaded_multipart_verify.bin')
        with open(downloaded_file_path, 'wb') as file:
            for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
                file.write(chunk)
        print('Object downloaded')

        assert filecmp.cmp(content_input_file, downloaded_file_path, shallow=False)

        os.remove(downloaded_file_path)

    def test_upload_manager_multipart_custom_parallel_process_count(self, object_storage, non_vcr_bucket, content_input_file):
        bucket = non_vcr_bucket
        object_name = 'test_object_multipart'
        namespace = object_storage.get_namespace().data

        part_size_in_bytes = (LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES - 1) * MEBIBYTE
        upload_manager = oci.object_storage.UploadManager(object_storage, allow_multipart_uploads=True, parallel_process_count=10)
        response = upload_manager.upload_file(
            namespace, bucket, object_name, content_input_file, part_size=part_size_in_bytes)
        util.validate_response(response)

        # confirm that the object was actually uploaded with multipart
        assert response.headers['opc-multipart-md5']

        print('Downloading object {} from {} for verification'.format(object_name, bucket))
        response = object_storage.get_object(
            namespace_name=namespace,
            bucket_name=bucket,
            object_name=object_name
        )
        downloaded_file_path = os.path.join('tests', 'resources', 'downloaded_multipart_verify.bin')
        with open(downloaded_file_path, 'wb') as file:
            for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
                file.write(chunk)
        print('Object downloaded')

        assert filecmp.cmp(content_input_file, downloaded_file_path, shallow=False)

        os.remove(downloaded_file_path)

    def test_upload_manager_multipart_disabled_with_large_file_uses_single_part(self, object_storage, non_vcr_bucket, content_input_file):
        object_name = 'test_object_multipart'
        namespace = object_storage.get_namespace().data

        # explicitly use part_size > file size to trigger multipart
        part_size_in_bytes = (LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES - 1) * MEBIBYTE
        upload_manager = oci.object_storage.UploadManager(object_storage, allow_multipart_uploads=False)
        response = upload_manager.upload_file(
            namespace, non_vcr_bucket, object_name, content_input_file, part_size=part_size_in_bytes)
        util.validate_response(response)

        # confirm that the object was actually uploaded with multipart
        assert response.headers['opc-content-md5']

    def test_upload_manager_multipart_resume_put(self, object_storage, non_vcr_bucket, content_input_file):
        # Tests that the resume works in the case of a multipart upload with last part < part_size
        UPLOAD_LAST_PART = [-1]

        # *** Case 1: part_size = 2 MB, file_size = 3 MB, last_part = 1 MB ***
        # File split into 2 parts (1st part of 2 MB, 2nd part of 1 MB)
        # Hence last_part < part_size
        part_size_in_bytes = 2 * MEBIBYTE
        self.multipart_resume_put(part_size_in_bytes, object_storage, non_vcr_bucket, content_input_file, UPLOAD_LAST_PART)

        # *** Case 2: part_size = 1 MB, file_size = 3 MB, last_part = 1 MB ***
        # File split into 3 parts (1st part of 1 MB, 2nd part of 1 MB, 3rd part of 1 MB)
        # Hence last_part = part_size
        part_size_in_bytes = 1 * MEBIBYTE
        self.multipart_resume_put(part_size_in_bytes, object_storage, non_vcr_bucket, content_input_file, UPLOAD_LAST_PART)

    def multipart_resume_put(self, part_size_in_bytes, object_storage, bucket, content_input_file, upload_part_nums):
        object_name = 'test_object_multipart_resume_put'
        namespace = object_storage.get_namespace().data

        kwargs = {'part_size': part_size_in_bytes}
        ma = MultipartObjectAssembler(object_storage, namespace, bucket, object_name, **kwargs)
        ma.new_upload()
        ma.add_parts_from_file(content_input_file)
        parts = list(enumerate(ma.manifest['parts']))

        # Upload the last part of the file
        for part_to_upload_num in upload_part_nums:
            ma._upload_part(part_num=parts[part_to_upload_num][0] + 1, part=parts[part_to_upload_num][1])

        upload_id = ma.manifest['uploadId']

        # Resume upload
        upload_manager = oci.object_storage.UploadManager(object_storage, allow_multipart_uploads=True)
        response = upload_manager.resume_upload_file(namespace, bucket, object_name, content_input_file,
                                                     upload_id, **kwargs)
        util.validate_response(response)

        # confirm that the object was actually uploaded with multipart
        assert response.headers['opc-multipart-md5']

        response = object_storage.get_object(
            namespace_name=namespace,
            bucket_name=bucket,
            object_name=object_name
        )
        downloaded_file_path = os.path.join('tests', 'resources', 'downloaded_file.bin')
        with open(downloaded_file_path, 'wb') as file:
            for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
                file.write(chunk)

        assert filecmp.cmp(content_input_file, downloaded_file_path, shallow=False)
        os.remove(downloaded_file_path)

    def test_upload_manager_piped_from_stream(self, object_storage, non_vcr_bucket, config_file, config_profile, config):
        if sys.platform == 'win32':
            pytest.skip("Stream piping tests don't run on Windows")

        bucket = non_vcr_bucket
        large_file_path = os.path.join('tests', 'resources', 'large_file.bin')
        util.create_large_file(large_file_path, 500)  # Make a 500 MiB file

        namespace = object_storage.get_namespace().data
        object_name = 'test_obj_piped_{}'.format(int(time.time()))

        print('cat-ing file and piping to script')
        cat_large_file = subprocess.Popen(['cat', large_file_path], stdout=subprocess.PIPE)
        call_return = subprocess.call(
            ['python', 'tests/scripts/upload_manager_from_stdin.py', config_file, config_profile, config['pass_phrase'], namespace, bucket, object_name],
            stdin=cat_large_file.stdout
        )
        cat_large_file.wait()
        assert call_return == 0
        print('Uploaded {} to Object Storage'.format(object_name))

        # For child processes there is a caveat:
        #
        # For RUSAGE_CHILDREN, this is the resident set size of the largest child, not the maximum resident set size of the
        # process tree.
        #
        # But as a rough test the largest child should be OK
        max_child_process_memory_utilisation = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss

        # In the script we have 10 threads processing stuff in the pool and they should be consuming 10 MiB each by default.
        # As such it should consume a max of 100 MiB, but we'll give it a bit of extra buffer since there's other stuff going
        # on besides the threads which are processing the file.
        #
        # From testing, the memory usage is higher on Python 2 but it is still less than the total size of the file
        if six.PY3:
            # Empirically, Python 3.5 is ~180 MiB memory usage but Python 3.6 is ~160 MiB
            max_size_limit_bytes = 180 * 1024 * 1024
        else:
            max_size_limit_bytes = 260 * 1024 * 2014

        assert max_child_process_memory_utilisation <= max_size_limit_bytes, 'Expected child process utilization {} to be <= limit {}'.format(max_child_process_memory_utilisation, max_size_limit_bytes)

        print('Downloading object {} from {} for verification'.format(object_name, bucket))
        response = object_storage.get_object(
            namespace_name=namespace,
            bucket_name=bucket,
            object_name=object_name
        )
        downloaded_large_file_path = os.path.join('tests', 'resources', 'downloaded_large_file.bin')
        with open(downloaded_large_file_path, 'wb') as file:
            for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
                file.write(chunk)
        print('Object downloaded')

        assert filecmp.cmp(large_file_path, downloaded_large_file_path, shallow=False)

        os.remove(downloaded_large_file_path)
        os.remove(large_file_path)

    def test_upload_manager_pipe_empty_file_from_stream(self, object_storage, non_vcr_bucket, config_file, config_profile, config):
        if sys.platform == 'win32':
            pytest.skip("Stream piping tests don't run on Windows")

        bucket = non_vcr_bucket
        test_file = get_resource_path('empty_file')

        namespace = object_storage.get_namespace().data
        object_name = 'test_obj_empty_piped_{}'.format(int(time.time()))

        print('cat-ing empty file and piping to script')
        cat_large_file = subprocess.Popen(['cat', test_file], stdout=subprocess.PIPE)
        call_return = subprocess.call(
            ['python', 'tests/scripts/upload_manager_from_stdin.py', config_file, config_profile, config['pass_phrase'], namespace, bucket, object_name],
            stdin=cat_large_file.stdout
        )
        cat_large_file.wait()
        assert call_return == 0
        print('Uploaded {} to Object Storage'.format(object_name))

        response = object_storage.get_object(
            namespace_name=namespace,
            bucket_name=bucket,
            object_name=object_name
        )
        downloaded_empty_file_path = os.path.join('tests', 'resources', 'downloaded_empty_file.bin')
        with open(downloaded_empty_file_path, 'wb') as file:
            for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
                file.write(chunk)
        print('Object downloaded')

        assert filecmp.cmp(test_file, downloaded_empty_file_path, shallow=False)

        os.remove(downloaded_empty_file_path)

    def test_upload_stream_from_ioBytes(self, object_storage, namespace, non_vcr_bucket):
        is_parallel = True
        num_threads = 8
        data_size = 4 * 1024 * 1024
        part_size = 512 * 1024
        object_name = "ioByteTest"
        # The data we are uploading
        b = b'0123456789abcdefg'
        data = (b * (data_size // len(b))) + (b'x' * (data_size % len(b)))
        assert len(data) == data_size
        # Upload
        s = io.BytesIO(data)
        print("Bucket: {}".format(non_vcr_bucket))
        print("Data length: {}".format(len(data)))
        upload_manager = UploadManager(object_storage,
                                       allow_parallel_uploads=is_parallel,
                                       parallel_process_count=num_threads)
        upload_manager.upload_stream(namespace, non_vcr_bucket, object_name, s, part_size=part_size)

        # Download
        get_result = object_storage.get_object(
            namespace_name=namespace,
            bucket_name=non_vcr_bucket,
            object_name=object_name,
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
        downloaded = bytearray(len(data))
        get_result.data.raw.readinto(downloaded)
        assert data == downloaded

    def test_upload_manager_multipart_ssec_kms(self, object_storage, non_vcr_bucket, content_input_file):
        object_name = 'test_object_multipart_ssec_kms'
        namespace = object_storage.get_namespace().data

        ssec_kms = "ocid1.key.oc1.phx.avnybakjaafna.abyhqljthy6bmiwubo3givln3agaswkfdrdlpvjgh2oyfgfsxnymwf7fb4sa"
        # explicitly use part_size < file size to trigger multipart
        part_size_in_bytes = (LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES - 1) * MEBIBYTE
        upload_manager = oci.object_storage.UploadManager(object_storage, allow_multipart_uploads=True)
        response = upload_manager.upload_file(
            namespace, non_vcr_bucket, object_name, content_input_file, part_size=part_size_in_bytes,
            opc_sse_kms_key_id=ssec_kms)
        util.validate_response(response)

        # confirm that the object was actually uploaded with multipart
        assert response.headers['opc-multipart-md5']

        print('Downloading object {} from {} for verification'.format(object_name, non_vcr_bucket))
        # downloading the object doesn't require sse kms key id to be passed
        response = object_storage.get_object(
            namespace_name=namespace,
            bucket_name=non_vcr_bucket,
            object_name=object_name,
        )
        downloaded_file_path = os.path.join('tests', 'resources', 'downloaded_multipart_ssec_kms_verify.bin')
        with open(downloaded_file_path, 'wb') as file:
            for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
                file.write(chunk)
        print('Object downloaded')

        assert filecmp.cmp(content_input_file, downloaded_file_path, shallow=False)

        os.remove(downloaded_file_path)
