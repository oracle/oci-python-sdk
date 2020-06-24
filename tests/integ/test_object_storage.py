# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.object_storage.transfer.constants import MEBIBYTE
from tests.util import get_resource_path, random_number_string, unique_name
from . import util
from .. import test_config_container
import base64
import filecmp
import hashlib
import oci
import os
import os.path
import pytest
from oci._vendor import requests

LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES = 3

# Static content for get_object tests
expected_content = "a/b/c/object3"


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
def set_up_test_data(object_storage, namespace):
    """
    set_up_test_data should only run once and it will ensure the namespace
    has the correct buckets, objects and meta data for all tests.
    """
    with test_config_container.create_vcr().use_cassette('test_object_storage_setup_test_data.yml'):
        result = util.ensure_test_data(object_storage, namespace, util.COMPARTMENT_ID, util.bucket_prefix())

    return result


# Response from GetObject for streaming tests
@pytest.fixture
def get_object_response(object_storage, namespace, set_up_test_data):
    assert set_up_test_data
    with test_config_container.create_vcr().use_cassette('test_object_storage_get_object_response.yml'):
        _response = object_storage.get_object(
            namespace_name=namespace,
            bucket_name=util.bucket_prefix() + "ReadOnlyTestBucket2",
            object_name=expected_content
        )
        assert _response.status == 200
        return _response


@pytest.fixture(scope="class")
def namespace(object_storage):
    return object_storage.get_namespace().data


@pytest.fixture
def bucket(object_storage, namespace, request):
    bucket_name = unique_name(request.node.name)
    response = create_bucket(object_storage, namespace, bucket_name)
    assert response.status == 200

    yield bucket_name

    delete_objects_in_bucket(object_storage, namespace, bucket_name)
    response = object_storage.delete_bucket(namespace, bucket_name)
    assert response.status == 204


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


class TestObjectStorage:

    def test_get_namespace(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_get_namespace.yml'):
            response = object_storage.get_namespace()
            assert response.status == 200

    def test_get_namespace_using_key_content(self, config):
        with test_config_container.create_vcr().use_cassette('test_object_storage_get_namespace_using_key_content.yml'):
            key_file = config['key_file']
            with open(key_file, 'rb') as f:
                key_content = f.read()

            del config['key_file']
            config['key_content'] = key_content

            client = oci.object_storage.ObjectStorageClient(config)
            response = client.get_namespace()
            assert response.status == 200

    def test_bucket_archive_crud(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_bucket_archive_crud.yml'):
            bucket_name = unique_name('test_bucket_archive')
            namespace = object_storage.get_namespace().data

            # Create
            request = oci.object_storage.models.CreateBucketDetails()
            request.name = bucket_name
            request.compartment_id = util.COMPARTMENT_ID
            request.storage_tier = 'Archive'
            response = object_storage.create_bucket(namespace, request)
            assert response.status == 200

            bucket = response.data
            assert bucket_name == bucket.name
            assert util.COMPARTMENT_ID == bucket.compartment_id
            assert 'Archive' == bucket.storage_tier

            # Get
            response = object_storage.get_bucket(namespace, bucket_name)
            assert response.status == 200
            assert bucket_name == response.data.name
            assert 'Archive' == response.data.storage_tier

            # Update
            request = oci.object_storage.models.UpdateBucketDetails()
            request.name = bucket_name
            request.metadata = {'new key': 'updated!', 'key2': 'another value'}
            response = object_storage.update_bucket(namespace, bucket_name, request)
            bucket = response.data
            assert response.status == 200
            assert 'updated!' == bucket.metadata['new key']
            assert 'another value' == bucket.metadata['key2']

            # Delete
            response = object_storage.delete_bucket(namespace, bucket_name)
            assert response.status == 204

    def test_bucket_crud(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_bucket_crud.yml'):
            bucket_name = unique_name('test_bucket')
            namespace = object_storage.get_namespace().data
            bucket_count = len(object_storage.list_buckets(namespace, util.COMPARTMENT_ID, limit=500).data)

            # Create
            request = oci.object_storage.models.CreateBucketDetails()
            request.name = bucket_name
            request.compartment_id = util.COMPARTMENT_ID
            request.metadata = {'some key': 'some example metadata'}
            response = object_storage.create_bucket(namespace, request)
            assert response.status == 200

            bucket = response.data
            assert type(bucket) is oci.object_storage.models.Bucket
            assert bucket_name == bucket.name
            assert 'some example metadata' == bucket.metadata['some key']

            # Get
            response = object_storage.get_bucket(namespace, bucket_name)
            assert response.status == 200
            assert type(response.data) is oci.object_storage.models.Bucket
            assert bucket_name == response.data.name
            assert response.data.freeform_tags == {}
            assert response.data.defined_tags == {}

            # List
            response = object_storage.list_buckets(namespace, util.COMPARTMENT_ID, limit=500)
            assert response.status == 200
            assert bucket_count + 1 == len(response.data)
            assert type(response.data[0]) is oci.object_storage.models.BucketSummary

            # Update
            request = oci.object_storage.models.UpdateBucketDetails()
            request.name = bucket_name
            request.metadata = {'new key': 'updated!', 'key2': 'another value'}
            response = object_storage.update_bucket(namespace, bucket_name, request)
            bucket = response.data
            assert response.status == 200
            assert type(bucket) is oci.object_storage.models.Bucket
            assert 'another value' == bucket.metadata['key2']

            # Delete
            response = object_storage.delete_bucket(namespace, bucket_name)
            assert response.status == 204

    def test_bucket_tagging(self, object_storage, identity):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_bucket_tagging.yml'):
            tag_ns = os.environ.get('OCI_PYSDK_APPLY_TAGS_TAG_NAMESPACE')
            tag_one = os.environ.get('OCI_PYSDK_APPLY_TAGS_TAG_ONE')
            tag_two = os.environ.get('OCI_PYSDK_APPLY_TAGS_TAG_TWO')
            bucket_name = unique_name('test_bucket_with_tags')
            namespace = object_storage.get_namespace().data

            # Create a bucket with tags
            response = object_storage.create_bucket(
                namespace,
                oci.object_storage.models.CreateBucketDetails(
                    name=bucket_name,
                    compartment_id=util.COMPARTMENT_ID,
                    freeform_tags={'one': '2', 'three': 'fourty_four'},
                    defined_tags={tag_ns: {tag_one: 'val one', tag_two: 'value 2'}}
                )
            )

            try:
                assert response.data.freeform_tags == {'one': '2', 'three': 'fourty_four'}
                assert response.data.defined_tags == {tag_ns: {tag_one: 'val one', tag_two: 'value 2'}}

                # The tags come back when getting the bucket
                get_bucket_response = object_storage.get_bucket(namespace, bucket_name)
                assert get_bucket_response.data.freeform_tags == {'one': '2', 'three': 'fourty_four'}
                assert get_bucket_response.data.defined_tags == {tag_ns: {tag_one: 'val one', tag_two: 'value 2'}}

                # I can update the tags with different values (these overwrite the existing values)
                update_bucket_response = object_storage.update_bucket(
                    namespace,
                    bucket_name,
                    oci.object_storage.models.UpdateBucketDetails(
                        name=bucket_name,
                        freeform_tags={'1': 'one'},
                        defined_tags={tag_ns: {tag_one: 'replaced'}}
                    )
                )
                assert update_bucket_response.data.freeform_tags == {'1': 'one'}
                assert update_bucket_response.data.defined_tags == {tag_ns: {tag_one: 'replaced'}}

                # An update with null tags preserves
                update_bucket_response = object_storage.update_bucket(
                    namespace,
                    bucket_name,
                    oci.object_storage.models.UpdateBucketDetails(
                        name=bucket_name,
                        public_access_type='ObjectReadWithoutList'
                    )
                )
                assert update_bucket_response.data.freeform_tags == {'1': 'one'}
                assert update_bucket_response.data.defined_tags == {tag_ns: {tag_one: 'replaced'}}

                # I can clear tags by passing an empty dict
                update_bucket_response = object_storage.update_bucket(
                    namespace,
                    bucket_name,
                    oci.object_storage.models.UpdateBucketDetails(
                        name=bucket_name,
                        freeform_tags={},
                        defined_tags={}
                    )
                )
                assert update_bucket_response.data.freeform_tags == {}
                assert update_bucket_response.data.defined_tags == {}

                get_bucket_response = object_storage.get_bucket(namespace, bucket_name)
                assert get_bucket_response.data.freeform_tags == {}
                assert get_bucket_response.data.defined_tags == {}
            finally:
                object_storage.delete_bucket(namespace, bucket_name)

    def test_object_crud(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_object_crud.yml'):
            # Setup a bucket to use.
            object_name_a = 'object_A'
            bucket_name = unique_name('test_object_CRUD')
            test_data = 'This is a test ' + random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''  # noqa: W605
            namespace = object_storage.get_namespace().data

            request = oci.object_storage.models.CreateBucketDetails()
            request.name = bucket_name
            request.compartment_id = util.COMPARTMENT_ID
            response = object_storage.create_bucket(namespace, request)
            assert response.status == 200

            # Put an object
            response = object_storage.put_object(namespace, bucket_name, object_name_a, test_data)
            assert response.status == 200

            # Get it back
            response = object_storage.get_object(namespace, bucket_name, object_name_a)
            assert response.status == 200
            response_text = response.data.content.decode('UTF-8')
            assert len(test_data) == len(response_text)
            assert test_data == response_text
            assert isinstance(response.data, requests.Response)

            # Head
            response = object_storage.head_object(namespace, bucket_name, object_name_a)
            assert response.status == 200
            assert len(test_data) == int(response.headers['content-length'])

            # Put a couple more objects
            object_storage.put_object(
                namespace, bucket_name, 'second_object', random_number_string())
            object_storage.put_object(
                namespace, bucket_name, 'third_object', random_number_string())

            # List
            response = object_storage.list_objects(namespace, bucket_name)
            assert response.status == 200
            object_list = response.data
            assert isinstance(object_list, oci.object_storage.models.ListObjects)
            assert 3 == len(object_list.objects)
            assert type(object_list.objects[0]) is oci.object_storage.models.ObjectSummary

            # Delete
            for summary in object_list.objects:
                response = object_storage.delete_object(namespace, bucket_name, summary.name)
                assert response.status == 204

            # Clean up
            response = object_storage.delete_bucket(namespace, bucket_name)
            assert response.status == 204

    def test_object_rename(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_object_rename.yml'):
            # Setup a bucket to use.
            object_name_a = 'object_A'
            object_name_b = 'object_B'
            bucket_name = unique_name('test_object_rename')
            test_data = 'This is a test ' + random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''  # noqa: W605
            namespace = object_storage.get_namespace().data

            request = oci.object_storage.models.CreateBucketDetails()
            request.name = bucket_name
            request.compartment_id = util.COMPARTMENT_ID
            response = object_storage.create_bucket(namespace, request)
            assert response.status == 200

            # Put an object
            response = object_storage.put_object(namespace, bucket_name, object_name_a, test_data, opc_meta={'foo1': 'bar1', 'foo2': 'bar2'})
            assert response.status == 200

            request = oci.object_storage.models.RenameObjectDetails()
            request.source_name = object_name_a
            request.new_name = object_name_b
            response = object_storage.rename_object(namespace, bucket_name, request)

            # Get it back by new name
            response = object_storage.get_object(namespace, bucket_name, object_name_b)
            assert response.status == 200
            response_text = response.data.content.decode('UTF-8')
            assert test_data == response_text
            assert 'bar1' == response.headers['opc-meta-foo1']
            assert 'bar2' == response.headers['opc-meta-foo2']

            # Head by new name
            response = object_storage.head_object(namespace, bucket_name, object_name_b)
            assert response.status == 200
            assert 'bar1' == response.headers['opc-meta-foo1']
            assert 'bar2' == response.headers['opc-meta-foo2']

            # Delete
            response = object_storage.delete_object(namespace, bucket_name, object_name_b)
            assert response.status == 204

            # Clean up
            response = object_storage.delete_bucket(namespace, bucket_name)
            assert response.status == 204

    def test_object_restore(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_object_restore.yml'):
            # Setup an archive bucket to use.
            bucket_name = unique_name('test_object_restore')
            namespace = object_storage.get_namespace().data

            request = oci.object_storage.models.CreateBucketDetails()
            request.name = bucket_name
            request.compartment_id = util.COMPARTMENT_ID
            request.storage_tier = 'Archive'
            response = object_storage.create_bucket(namespace, request)
            assert response.status == 200

            self.restore_object_internal(object_storage, namespace, bucket_name, 'object_A')
            self.restore_object_internal(object_storage, namespace, bucket_name, 'object_A', 100)

            # Clean up
            response = object_storage.delete_bucket(namespace, bucket_name)
            assert response.status == 204

    def test_object_crud_with_metadata(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_object_crud_with_metadata.yml'):
            # Setup a bucket to use.
            object_name_a = 'object_A'
            bucket_name = unique_name('test_object_CRUD_with_metadata')
            test_data = 'This is a test ' + random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''  # noqa: W605
            namespace = object_storage.get_namespace().data

            request = oci.object_storage.models.CreateBucketDetails()
            request.name = bucket_name
            request.compartment_id = util.COMPARTMENT_ID
            response = object_storage.create_bucket(namespace, request)
            assert response.status == 200

            # Put an object
            response = object_storage.put_object(
                namespace, bucket_name, object_name_a, test_data,
                opc_meta={'foo1': 'bar1', 'foo2': 'bar2'})
            assert response.status == 200

            # Get it back
            response = object_storage.get_object(namespace, bucket_name, object_name_a)
            assert response.status == 200
            response_text = response.data.content.decode('UTF-8')
            assert len(test_data) == len(response_text)
            assert test_data == response_text
            assert isinstance(response.data, requests.Response)
            assert 'bar1' == response.headers['opc-meta-foo1']
            assert 'bar2' == response.headers['opc-meta-foo2']

            # Head
            response = object_storage.head_object(namespace, bucket_name, object_name_a)
            assert response.status == 200
            assert len(test_data) == int(response.headers['content-length'])
            assert 'bar1' == response.headers['opc-meta-foo1']
            assert 'bar2' == response.headers['opc-meta-foo2']

            # Delete
            response = object_storage.delete_object(namespace, bucket_name, object_name_a)
            assert response.status == 204

            # Clean up
            response = object_storage.delete_bucket(namespace, bucket_name)
            assert response.status == 204

    def test_put_empty_file(self, object_storage):
        # Setup a bucket to use.
        object_name = 'empty_object'
        bucket_name = unique_name('test_object_CRUD', ignore_vcr=True)
        namespace = object_storage.get_namespace().data
        test_file = get_resource_path('empty_file')

        request = oci.object_storage.models.CreateBucketDetails()
        request.name = bucket_name
        request.compartment_id = util.COMPARTMENT_ID
        response = object_storage.create_bucket(namespace, request)
        assert response.status == 200

        # Put empty file
        with open(test_file, 'rb') as file:
            response = object_storage.put_object(namespace, bucket_name, object_name, file)
            assert response.status == 200

        # Get it back
        response = object_storage.get_object(namespace, bucket_name, object_name)
        assert response.status == 200
        response_text = response.data.content.decode('UTF-8')
        assert 0 == len(response_text)

        # Head
        response = object_storage.head_object(namespace, bucket_name, object_name)
        assert response.status == 200
        assert 0 == int(response.headers['content-length'])

        # Clean up
        response = object_storage.delete_object(namespace, bucket_name, object_name)
        assert response.status == 204
        response = object_storage.delete_bucket(namespace, bucket_name)
        assert response.status == 204

    def test_put_empty_string(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_put_empty_string.yml'):
            # Setup a bucket to use.
            object_name = 'empty_object'
            bucket_name = unique_name('test_object_CRUD')
            namespace = object_storage.get_namespace().data

            request = oci.object_storage.models.CreateBucketDetails()
            request.name = bucket_name
            request.compartment_id = util.COMPARTMENT_ID
            response = object_storage.create_bucket(namespace, request)
            assert response.status == 200

            # Put empty string
            response = object_storage.put_object(namespace, bucket_name, object_name, '')
            assert response.status == 200

            # Get it back
            response = object_storage.get_object(namespace, bucket_name, object_name)
            assert response.status == 200
            response_text = response.data.content.decode('UTF-8')
            assert 0 == len(response_text)

            # Head
            response = object_storage.head_object(namespace, bucket_name, object_name)
            assert response.status == 200
            assert 0 == int(response.headers['content-length'])

            # Clean up
            response = object_storage.delete_object(namespace, bucket_name, object_name)
            assert response.status == 204
            response = object_storage.delete_bucket(namespace, bucket_name)
            assert response.status == 204

    def test_put_with_int_content_length(self, object_storage):
        # Setup test
        object_name = 'int_content_length'
        bucket_name = unique_name('test_object_CRUD', ignore_vcr=True)
        namespace = object_storage.get_namespace().data
        int_content_length = 9
        data = b'123456789'

        # Create the bucket
        request = oci.object_storage.models.CreateBucketDetails()
        request.name = bucket_name
        request.compartment_id = util.COMPARTMENT_ID
        response = object_storage.create_bucket(namespace, request)
        assert response.status == 200

        # Put the object
        object_storage.put_object(
            namespace_name=namespace,
            bucket_name=bucket_name,
            object_name=object_name,
            put_object_body=data,
            content_length=int_content_length)

        # Get it back
        response = object_storage.get_object(namespace, bucket_name, object_name)
        assert response.status == 200
        response_text = response.data.content
        assert response_text == data
        assert int_content_length == len(response_text)

        # Verify object length stored in the head
        response = object_storage.head_object(namespace, bucket_name, object_name)
        assert response.status == 200
        assert int_content_length == int(response.headers['content-length'])

        # Clean up
        response = object_storage.delete_object(namespace, bucket_name, object_name)
        assert response.status == 204
        response = object_storage.delete_bucket(namespace, bucket_name)
        assert response.status == 204

    def test_put_readable_custom_content_length(self, object_storage, namespace, bucket):
        """User-provided content length is used when a readable without a length is provided."""
        class ReadableData(object):
            def __init__(self, data):
                self.data = data

            def read(self, n=0):
                if not self.data:
                    return None
                char, self.data = self.data[:1], self.data[1:]
                return char

        data = b"hello, world"
        readable_data = ReadableData(data)
        obj = unique_name("put_streaming_content_length")

        resp = object_storage.put_object(namespace, bucket, obj, readable_data, content_length=str(len(data)))
        assert resp.status == 200

        response = object_storage.get_object(namespace, bucket, obj)
        assert response.status == 200
        assert response.data.content == data

    def test_bucket_not_found(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_bucket_not_found.yml'):
            namespace = object_storage.get_namespace().data

            with pytest.raises(oci.exceptions.ServiceError) as excinfo:
                object_storage.get_bucket(namespace, unique_name('does_not_exist'))

            assert excinfo.value.status == 404

    def test_get_bucket(self, object_storage, set_up_test_data):
        assert set_up_test_data
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_get_bucket.yml'):
            namespace = object_storage.get_namespace().data
            response = object_storage.get_bucket(namespace, util.bucket_prefix() + 'ReadOnlyTestBucket1')
            assert response.status == 200
            assert type(response.data) is oci.object_storage.models.Bucket
            assert response.data.metadata is not None
            assert 0 == len(response.data.metadata)

    def test_get_bucket_with_metadata(self, object_storage, set_up_test_data):
        assert set_up_test_data
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_get_bucket_with_metadata.yml'):
            namespace = object_storage.get_namespace().data
            response = object_storage.get_bucket(namespace, util.bucket_prefix() + 'ReadOnlyTestBucket5')
            assert response.status == 200
            assert type(response.data) is oci.object_storage.models.Bucket
            assert response.data.metadata is not None
            assert 'bar1' == response.data.metadata['foo1']
            assert 'bar2' == response.data.metadata['foo2']

    def test_list_buckets(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_list_buckets.yml'):
            namespace = object_storage.get_namespace().data
            response = object_storage.list_buckets(namespace, util.COMPARTMENT_ID)
            assert response.status == 200
            assert len(response.data) > 0
            assert type(response.data[0]) is oci.object_storage.models.BucketSummary
            for bucket_summary in response.data:
                # These should be None as we did not ask for them in the request
                assert bucket_summary.defined_tags is None
                assert bucket_summary.freeform_tags is None

            response_with_tags = object_storage.list_buckets(namespace, util.COMPARTMENT_ID, fields=['tags'])
            assert response.status == 200
            assert len(response.data) > 0
            for bucket_summary in response_with_tags.data:
                # We've explicitly asked for tags, so should not get None back
                assert bucket_summary.defined_tags is not None
                assert bucket_summary.freeform_tags is not None

    def test_list_buckets_truncated(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_list_buckets_truncated.yml'):
            namespace = object_storage.get_namespace().data
            response = object_storage.list_buckets(namespace, util.COMPARTMENT_ID, limit=2)
            assert response.status == 200
            assert 2 == len(response.data)
            assert type(response.data[0]) is oci.object_storage.models.BucketSummary
            assert response.has_next_page
            first_bucket_name = response.data[0].name

            response = object_storage.list_buckets(
                namespace, util.COMPARTMENT_ID, limit=2, page=response.next_page)
            assert response.status == 200
            assert 2 == len(response.data)
            assert first_bucket_name != response.data[0].name

    def test_get_object(self, object_storage, set_up_test_data):
        assert set_up_test_data
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_get_object.yml'):
            namespace = object_storage.get_namespace().data
            response = object_storage.get_object(namespace, util.bucket_prefix() + 'ReadOnlyTestBucket1', 'object1')
            assert response.status == 200
            assert isinstance(response.data, requests.Response)

    def test_get_object_with_user_metadata(self, object_storage, set_up_test_data):
        assert set_up_test_data
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_get_object_with_user_metadata.yml'):
            namespace = object_storage.get_namespace().data
            response = object_storage.get_object(namespace, util.bucket_prefix() + 'ReadOnlyTestBucket4', 'hasUserMetadata.json')
            assert response.status == 200
            assert isinstance(response.data, requests.Response)
            assert 'bar1' == response.headers['opc-meta-foo1']
            assert 'bar2' == response.headers['opc-meta-foo2']

    def test_list_objects(self, object_storage, set_up_test_data):
        assert set_up_test_data
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_list_objects.yml'):
            namespace = object_storage.get_namespace().data
            response = object_storage.list_objects(namespace, util.bucket_prefix() + 'ReadOnlyTestBucket1')
            assert response.status == 200
            assert type(response.data) is oci.object_storage.models.ListObjects
            assert 5 == len(response.data.objects)
            assert response.data.prefixes is None

    def test_list_objects_empty_bucket(self, object_storage, set_up_test_data):
        assert set_up_test_data
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_list_objects_empty_bucket.yml'):
            namespace = object_storage.get_namespace().data
            response = object_storage.list_objects(namespace, util.bucket_prefix() + 'ReadOnlyTestBucket5')
            assert response.status == 200
            assert type(response.data) is oci.object_storage.models.ListObjects
            assert 0 == len(response.data.objects)
            assert response.data.prefixes is None

    def test_list_objects_with_prefix_and_delimiter(self, object_storage, set_up_test_data):
        assert set_up_test_data
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_list_objects_with_prefix_and_delimiter.yml'):
            namespace = object_storage.get_namespace().data
            response = object_storage.list_objects(
                namespace, util.bucket_prefix() + 'ReadOnlyTestBucket2', prefix='a/b/', delimiter='/')
            assert response.status == 200
            assert type(response.data) is oci.object_storage.models.ListObjects
            assert 2 == len(response.data.objects)
            assert 1 == len(response.data.prefixes)
            assert response.data.next_start_with is None

    def test_list_objects_truncated(self, object_storage, set_up_test_data):
        assert set_up_test_data
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_list_objects_truncated.yml'):
            namespace = object_storage.get_namespace().data
            response = object_storage.list_objects(namespace, util.bucket_prefix() + 'ReadOnlyTestBucket1', limit=3)
            assert response.status == 200
            assert type(response.data) is oci.object_storage.models.ListObjects
            assert len(response.data.objects) == 3
            assert response.data.prefixes is None
            assert response.data.next_start_with is not None
            first_object_name = response.data.objects[0].name

            response = object_storage.list_objects(
                namespace, util.bucket_prefix() + 'ReadOnlyTestBucket1', start=response.data.next_start_with)
            assert 2 == len(response.data.objects)
            assert response.data.prefixes is None
            assert response.data.next_start_with is None
            assert first_object_name != response.data.objects[0].name

    def test_head_object(self, object_storage, set_up_test_data):
        assert set_up_test_data
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_head_object.yml'):
            namespace = object_storage.get_namespace().data
            response = object_storage.head_object(namespace, util.bucket_prefix() + 'ReadOnlyTestBucket4', 'hasUserMetadata.json')
            assert response.status == 200
            assert response.data is None
            assert 'bar1' == response.headers['opc-meta-foo1']
            assert 'bar2' == response.headers['opc-meta-foo2']

    def test_head_not_found(self, object_storage, set_up_test_data):
        assert set_up_test_data
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_head_not_found.yml'):
            namespace = object_storage.get_namespace().data
            # Bucket exists, unknown key
            with pytest.raises(oci.exceptions.ServiceError) as excinfo:
                object_storage.head_object(
                    namespace, util.bucket_prefix() + "ReadOnlyTestBucket4", "unknown-key" + random_number_string())
            assert excinfo.value.status == 404
            # Unknown bucket, key exists
            with pytest.raises(oci.exceptions.ServiceError) as excinfo:
                object_storage.head_object(
                    namespace, "unknown-bucket" + random_number_string(), "hasUserMetadata.json")
            assert excinfo.value.status == 404

    def test_content(self, get_object_response):
        assert expected_content == get_object_response.data.content.decode('UTF-8')

    def test_iter_content(self, get_object_response):
        response_text = ''
        chunk_count = 0
        chunk_size = 2
        for chunk in get_object_response.data.iter_content(chunk_size=chunk_size):
            response_text += chunk.decode('UTF-8')
            chunk_count += 1

        assert chunk_count >= (len(expected_content) / chunk_size)
        assert response_text == expected_content

    def test_raw(self, get_object_response):
        response_text = get_object_response.data.raw.read(100).decode('UTF-8')
        assert response_text == expected_content

    def test_content_multiple_access(self, get_object_response):
        assert expected_content == get_object_response.data.content.decode('UTF-8')
        assert expected_content == get_object_response.data.content.decode('UTF-8')
        assert expected_content == get_object_response.data.content.decode('UTF-8')

    def test_stream_after_content(self, get_object_response):
        assert expected_content == get_object_response.data.content.decode('UTF-8')

        response_text = ''
        chunk_count = 0
        chunk_size = 2
        for chunk in get_object_response.data.iter_content(chunk_size=chunk_size):
            response_text += chunk.decode('UTF-8')
            chunk_count += 1

        assert chunk_count >= (len(expected_content) / chunk_size)
        assert response_text == expected_content

    def test_content_after_stream(self, get_object_response):
        response_text = ''
        for chunk in get_object_response.data.iter_content():
            response_text += chunk.decode('UTF-8')
        assert response_text == expected_content

        with pytest.raises(RuntimeError):
            # content was already consumed by iter_content above
            getattr(get_object_response.data, "content")

    def test_stream_twice(self, get_object_response):
        response_text = ''
        for chunk in get_object_response.data.iter_content():
            response_text += chunk.decode('UTF-8')
        assert response_text == expected_content

        with pytest.raises(requests.exceptions.StreamConsumedError):
            for chunk in get_object_response.data.iter_content():
                response_text += chunk.decode('UTF-8')

    def test_paging_list_objects(self, object_storage):
        with test_config_container.create_vcr().use_cassette('test_object_storage_test_paging_list_objects.yml'):
            created_bucket = None
            namespace = object_storage.get_namespace().data
            try:
                bucket_name = unique_name('PySdkPagingListObjects')
                create_bucket_response = object_storage.create_bucket(
                    namespace,
                    oci.object_storage.models.CreateBucketDetails(
                        compartment_id=util.COMPARTMENT_ID,
                        name=bucket_name
                    )
                )
                created_bucket = create_bucket_response.data

                for r in range(100):
                    object_storage.put_object(namespace, bucket_name, 'TestObj_{}'.format(r), 'Content for TestObj_{}'.format(r))

                all_objects_response = oci.pagination.list_call_get_all_results(
                    object_storage.list_objects,
                    namespace,
                    bucket_name
                )
                all_object_names = set([obj.name for obj in all_objects_response.data.objects])
                assert len(all_objects_response.data.objects) == 100
                assert len(all_object_names) == 100
                for r in range(100):
                    assert 'TestObj_{}'.format(r) in all_object_names

                objects_up_to_limit_response = oci.pagination.list_call_get_up_to_limit(
                    object_storage.list_objects,
                    50,
                    5,
                    namespace,
                    bucket_name
                )
                object_names = set([obj.name for obj in objects_up_to_limit_response.data.objects])
                assert len(objects_up_to_limit_response.data.objects) == 50
                assert len(object_names) == 50
                for obj_name in object_names:
                    assert 'TestObj_' in obj_name

                # Test the record generators explicitly. The response generators are already invoked via
                # list_call_get_all_results and list_call_get_up_to_limit
                all_objects_record_generator = oci.pagination.list_call_get_all_results_generator(
                    object_storage.list_objects,
                    'record',
                    namespace,
                    bucket_name
                )
                num_objects = 0
                for object_summary in all_objects_record_generator:
                    assert isinstance(object_summary, oci.object_storage.models.ObjectSummary)
                    assert 'TestObj_' in object_summary.name
                    num_objects += 1
                assert num_objects == 100

                objects_to_limit_generator = oci.pagination.list_call_get_up_to_limit_generator(
                    object_storage.list_objects,
                    90,
                    5,
                    'record',
                    namespace,
                    bucket_name
                )
                num_objects = 0
                for object_summary in objects_to_limit_generator:
                    assert isinstance(object_summary, oci.object_storage.models.ObjectSummary)
                    assert 'TestObj_' in object_summary.name
                    num_objects += 1
                assert num_objects == 90

                # There are only 100 objects, so sanity test we don't keep making requests over that limit
                objects_to_limit_generator = oci.pagination.list_call_get_up_to_limit_generator(
                    object_storage.list_objects,
                    200,
                    5,
                    'record',
                    namespace,
                    bucket_name
                )
                num_objects = 0
                for object_summary in objects_to_limit_generator:
                    assert isinstance(object_summary, oci.object_storage.models.ObjectSummary)
                    assert 'TestObj_' in object_summary.name
                    num_objects += 1
                assert num_objects == 100
            finally:
                if created_bucket:
                    all_objects_response = oci.pagination.list_call_get_all_results(
                        object_storage.list_objects,
                        namespace,
                        bucket_name
                    )
                    for obj in all_objects_response.data.objects:
                        object_storage.delete_object(created_bucket.namespace, created_bucket.name, obj.name)

                object_storage.delete_bucket(created_bucket.namespace, created_bucket.name)

    def restore_object_internal(self, object_storage, namespace, bucket_name, object_name, restore_hours=None):
        test_data = 'This is a test ' + random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''  # noqa: W605

        # Put an object
        response = object_storage.put_object(namespace, bucket_name, object_name, test_data)
        assert response.status == 200

        # Head
        response = object_storage.head_object(namespace, bucket_name, object_name)
        assert response.status == 200
        assert 'Archived' == response.headers['archival-state']

        # Cannot get object back when it's in archived state
        with pytest.raises(oci.exceptions.ServiceError) as excinfo:
            object_storage.get_object(namespace, bucket_name, object_name)
        assert excinfo.value.status == 409

        # Restore the object, it takes 24 hours
        request = oci.object_storage.models.RestoreObjectsDetails()
        request.object_name = object_name
        if restore_hours:
            request.hours = restore_hours
        response = object_storage.restore_objects(namespace, bucket_name, request)
        assert response.status >= 200 and response.status <= 299

        # Head again and verify archival state
        response = object_storage.head_object(namespace, bucket_name, object_name)
        assert response.status == 200
        assert 'Restoring' == response.headers['archival-state']

        # Delete
        response = object_storage.delete_object(namespace, bucket_name, object_name)
        assert response.status == 204

    def test_upload_manager_multipart_ssec(self, object_storage, non_vcr_bucket, content_input_file):
        object_name = 'test_object_multipart_ssec'
        namespace = object_storage.get_namespace().data

        ssec_key_bytes = os.urandom(32)
        ssec_key_str = base64.b64encode(ssec_key_bytes).decode('utf-8')
        ssec_key_sha256 = hashlib.sha256(ssec_key_bytes).digest()
        ssec_key_sha256_str = base64.b64encode(ssec_key_sha256).decode('utf-8')

        # explicitly use part_size < file size to trigger multipart
        part_size_in_bytes = (LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES - 1) * MEBIBYTE
        upload_manager = oci.object_storage.UploadManager(object_storage, allow_multipart_uploads=True)
        response = upload_manager.upload_file(
            namespace, non_vcr_bucket, object_name, content_input_file, part_size=part_size_in_bytes,
            opc_sse_customer_algorithm='AES256', opc_sse_customer_key=ssec_key_str,
            opc_sse_customer_key_sha256=ssec_key_sha256_str)
        util.validate_response(response)

        # confirm that the object was actually uploaded with multipart
        assert response.headers['opc-multipart-md5']

        print('Downloading object {} from {} for verification'.format(object_name, non_vcr_bucket))
        # downloading the object without supplying SSE-C parameters should fail
        with pytest.raises(oci.exceptions.ServiceError) as excinfo:
            object_storage.get_object(
                namespace_name=namespace,
                bucket_name=non_vcr_bucket,
                object_name=object_name
            )
        assert excinfo.value.status == 400
        response = object_storage.get_object(
            namespace_name=namespace,
            bucket_name=non_vcr_bucket,
            object_name=object_name,
            opc_sse_customer_algorithm='AES256',
            opc_sse_customer_key=ssec_key_str,
            opc_sse_customer_key_sha256=ssec_key_sha256_str
        )
        downloaded_file_path = os.path.join('tests', 'resources', 'downloaded_multipart_ssec_verify.bin')
        with open(downloaded_file_path, 'wb') as file:
            for chunk in response.data.raw.stream(MEBIBYTE, decode_content=False):
                file.write(chunk)
        print('Object downloaded')

        assert filecmp.cmp(content_input_file, downloaded_file_path, shallow=False)

        os.remove(downloaded_file_path)
