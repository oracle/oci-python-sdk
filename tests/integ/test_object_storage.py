from tests.util import get_resource_path, random_number_string, unique_name
import oraclebmc
import pytest
import requests
from . import util

# Static content for get_object tests
expected_content = "a/b/c/object3"


# Response from GetObject for streaming tests
@pytest.fixture
def get_object_response(object_storage):
    _response = object_storage.get_object(
        namespace_name="internalbriangustafson",
        bucket_name="ReadOnlyTestBucket2",
        object_name=expected_content
    )
    assert _response.status == 200
    return _response


@pytest.fixture
def namespace(object_storage):
    return object_storage.get_namespace().data


@pytest.yield_fixture
def bucket(object_storage, namespace, request):
    bucket_name = unique_name(request.node.name)
    request = oraclebmc.object_storage.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = util.COMPARTMENT_ID
    response = object_storage.create_bucket(namespace, request)
    assert response.status == 200

    yield bucket_name

    for obj in object_storage.list_objects(namespace, bucket_name).data.objects:
        object_storage.delete_object(namespace, bucket_name, obj.name)
    response = object_storage.delete_bucket(namespace, bucket_name)
    assert response.status == 204


class TestObjectStorage:
    def test_get_namespace(self, object_storage):
        response = object_storage.get_namespace()
        assert response.status == 200

    def test_bucket_crud(self, object_storage):
        bucket_name = unique_name('test_bucket')
        namespace = object_storage.get_namespace().data
        bucket_count = len(object_storage.list_buckets(namespace, util.COMPARTMENT_ID, limit=500).data)

        # Create
        request = oraclebmc.object_storage.models.CreateBucketDetails()
        request.name = bucket_name
        request.compartment_id = util.COMPARTMENT_ID
        request.metadata = {'some key': 'some example metadata'}
        response = object_storage.create_bucket(namespace, request)
        assert response.status == 200

        bucket = response.data
        assert type(bucket) is oraclebmc.object_storage.models.Bucket
        assert bucket_name == bucket.name
        assert 'some example metadata' == bucket.metadata['some key']

        # Get
        response = object_storage.get_bucket(namespace, bucket_name)
        assert response.status == 200
        assert type(response.data) is oraclebmc.object_storage.models.Bucket
        assert bucket_name == response.data.name

        # List
        response = object_storage.list_buckets(namespace, util.COMPARTMENT_ID, limit=500)
        assert response.status == 200
        assert bucket_count + 1 == len(response.data)
        assert type(response.data[0]) is oraclebmc.object_storage.models.BucketSummary

        # Update
        request = oraclebmc.object_storage.models.UpdateBucketDetails()
        request.name = bucket_name
        request.metadata = {'new key': 'updated!', 'key2': 'another value'}
        response = object_storage.update_bucket(namespace, bucket_name, request)
        bucket = response.data
        assert response.status == 200
        assert type(bucket) is oraclebmc.object_storage.models.Bucket
        assert 'another value' == bucket.metadata['key2']

        # Delete
        response = object_storage.delete_bucket(namespace, bucket_name)
        assert response.status == 204

    def test_object_crud(self, object_storage):
        # Setup a bucket to use.
        object_name_a = 'object_A'
        bucket_name = unique_name('test_object_CRUD')
        test_data = 'This is a test ' + random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''
        namespace = object_storage.get_namespace().data

        request = oraclebmc.object_storage.models.CreateBucketDetails()
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
        assert isinstance(object_list, oraclebmc.object_storage.models.ListObjects)
        assert 3 == len(object_list.objects)
        assert type(object_list.objects[0]) is oraclebmc.object_storage.models.ObjectSummary

        # Delete
        for summary in object_list.objects:
            response = object_storage.delete_object(namespace, bucket_name, summary.name)
            assert response.status == 204

        # Clean up
        response = object_storage.delete_bucket(namespace, bucket_name)
        assert response.status == 204

    def test_object_crud_with_metadata(self, object_storage):
        # Setup a bucket to use.
        object_name_a = 'object_A'
        bucket_name = unique_name('test_object_CRUD_with_metadata')
        test_data = 'This is a test ' + random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''
        namespace = object_storage.get_namespace().data

        request = oraclebmc.object_storage.models.CreateBucketDetails()
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
        bucket_name = unique_name('test_object_CRUD')
        namespace = object_storage.get_namespace().data
        test_file = get_resource_path('empty_file')

        request = oraclebmc.object_storage.models.CreateBucketDetails()
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
        # Setup a bucket to use.
        object_name = 'empty_object'
        bucket_name = unique_name('test_object_CRUD')
        namespace = object_storage.get_namespace().data

        request = oraclebmc.object_storage.models.CreateBucketDetails()
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

    def test_put_readable_custom_content_length(self, object_storage, namespace, bucket):
        """User-provided content length is used when a readable without a length is provided."""
        class ReadableData(object):
            def __init__(self, data):
                self.data = data

            def read(self, n):
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
        namespace = object_storage.get_namespace().data

        with pytest.raises(oraclebmc.exceptions.ServiceError) as excinfo:
            object_storage.get_bucket(namespace, unique_name('does_not_exist'))

        assert excinfo.value.status == 404

    def test_get_bucket(self, object_storage):
        namespace = object_storage.get_namespace().data
        response = object_storage.get_bucket(namespace, 'ReadOnlyTestBucket1')
        assert response.status == 200
        assert type(response.data) is oraclebmc.object_storage.models.Bucket
        assert response.data.metadata is not None
        assert 0 == len(response.data.metadata)

    def test_get_bucket_with_metadata(self, object_storage):
        namespace = object_storage.get_namespace().data
        response = object_storage.get_bucket(namespace, 'ReadOnlyTestBucket5')
        assert response.status == 200
        assert type(response.data) is oraclebmc.object_storage.models.Bucket
        assert response.data.metadata is not None
        assert 'bar1' == response.data.metadata['foo1']
        assert 'bar2' == response.data.metadata['foo2']

    def test_list_buckets(self, object_storage):
        namespace = object_storage.get_namespace().data
        response = object_storage.list_buckets(namespace, util.COMPARTMENT_ID)
        assert response.status == 200
        assert len(response.data) > 0
        assert type(response.data[0]) is oraclebmc.object_storage.models.BucketSummary

    def test_list_buckets_truncated(self, object_storage):
        namespace = object_storage.get_namespace().data
        response = object_storage.list_buckets(namespace, util.COMPARTMENT_ID, limit=2)
        assert response.status == 200
        assert 2 == len(response.data)
        assert type(response.data[0]) is oraclebmc.object_storage.models.BucketSummary
        assert response.has_next_page
        first_bucket_name = response.data[0].name

        response = object_storage.list_buckets(
            namespace, util.COMPARTMENT_ID, limit=2, page=response.next_page)
        assert response.status == 200
        assert 2 == len(response.data)
        assert first_bucket_name != response.data[0].name

    def test_get_object(self, object_storage):
        namespace = object_storage.get_namespace().data
        response = object_storage.get_object(namespace, 'ReadOnlyTestBucket1', 'object1')
        assert response.status == 200
        assert isinstance(response.data, requests.Response)

    def test_get_object_with_user_metadata(self, object_storage):
        namespace = object_storage.get_namespace().data
        response = object_storage.get_object(namespace, 'ReadOnlyTestBucket4', 'hasUserMetadata.json')
        assert response.status == 200
        assert isinstance(response.data, requests.Response)
        assert 'bar1' == response.headers['opc-meta-foo1']
        assert 'bar2' == response.headers['opc-meta-foo2']

    def test_list_objects(self, object_storage):
        namespace = object_storage.get_namespace().data
        response = object_storage.list_objects(namespace, 'ReadOnlyTestBucket1')
        assert response.status == 200
        assert type(response.data) is oraclebmc.object_storage.models.ListObjects
        assert 5 == len(response.data.objects)
        assert response.data.prefixes is None

    def test_list_objects_empty_bucket(self, object_storage):
        namespace = object_storage.get_namespace().data
        response = object_storage.list_objects(namespace, 'ReadOnlyTestBucket5')
        assert response.status == 200
        assert type(response.data) is oraclebmc.object_storage.models.ListObjects
        assert 0 == len(response.data.objects)
        assert response.data.prefixes is None

    def test_list_objects_with_prefix_and_delimiter(self, object_storage):
        namespace = object_storage.get_namespace().data
        response = object_storage.list_objects(
            namespace, 'ReadOnlyTestBucket2', prefix='a/b/', delimiter='/')
        assert response.status == 200
        assert type(response.data) is oraclebmc.object_storage.models.ListObjects
        assert 2 == len(response.data.objects)
        assert 1 == len(response.data.prefixes)
        assert response.data.next_start_with is None

    def test_list_objects_truncated(self, object_storage):
        namespace = object_storage.get_namespace().data
        response = object_storage.list_objects(namespace, 'ReadOnlyTestBucket1', limit=3)
        assert response.status == 200
        assert type(response.data) is oraclebmc.object_storage.models.ListObjects
        assert len(response.data.objects) == 3
        assert response.data.prefixes is None
        assert response.data.next_start_with is not None
        first_object_name = response.data.objects[0].name

        response = object_storage.list_objects(
            namespace, 'ReadOnlyTestBucket1', start=response.data.next_start_with)
        assert 2 == len(response.data.objects)
        assert response.data.prefixes is None
        assert response.data.next_start_with is None
        assert first_object_name != response.data.objects[0].name

    def test_head_object(self, object_storage):
        namespace = object_storage.get_namespace().data
        response = object_storage.head_object(namespace, 'ReadOnlyTestBucket4', 'hasUserMetadata.json')
        assert response.status == 200
        assert response.data is None
        assert 'bar1' == response.headers['opc-meta-foo1']
        assert 'bar2' == response.headers['opc-meta-foo2']

    def test_head_not_found(self, object_storage):
        namespace = object_storage.get_namespace().data
        # Bucket exists, unknown key
        with pytest.raises(oraclebmc.exceptions.ServiceError) as excinfo:
            object_storage.head_object(
                namespace, "ReadOnlyTestBucket4", "unknown-key" + random_number_string())
        assert excinfo.value.status == 404
        # Unknown bucket, key exists
        with pytest.raises(oraclebmc.exceptions.ServiceError) as excinfo:
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


def test_list_multipart_uploads_empty_bucket(object_storage, bucket):
    namespace = object_storage.get_namespace().data
    response = object_storage.list_multipart_uploads(namespace, bucket)
    assert response.status == 200
    assert type(response.data) is list
    assert 0 == len(response.data)


def test_list_multipart_uploads(object_storage, bucket):
    object_name = "test_multipart_file"
    namespace = object_storage.get_namespace().data
    request = oraclebmc.object_storage.models.CreateMultipartUploadDetails()
    request.object = object_name
    request.content_encoding = "gzip, deflate"
    request.content_type = "application/octet-stream"
    response = object_storage.create_multipart_upload(namespace, bucket, request)
    assert response.status == 200

    upload_id = response.data.upload_id

    response = object_storage.list_multipart_uploads(namespace, bucket)
    assert response.status == 200
    assert 1 == len(response.data)
    assert type(response.data[0]) is oraclebmc.object_storage.models.MultipartUpload
    assert response.data[0].upload_id == upload_id
    # Abort the upload since it was only created to make sure list works.
    response = object_storage.abort_multipart_upload(namespace,
                                                     bucket,
                                                     object_name,
                                                     upload_id)

    assert response.status == 204

    # Verify the upload_id no longer exists.
    with pytest.raises(oraclebmc.exceptions.ServiceError):
        response = object_storage.list_multipart_upload_parts(namespace,
                                                              bucket,
                                                              object_name,
                                                              upload_id)
        assert response.status == 404


def test_create_multipart_upload(object_storage, bucket):
    namespace = object_storage.get_namespace().data
    request = oraclebmc.object_storage.models.CreateMultipartUploadDetails()
    request.object = "test_multipart_file"
    request.content_encoding = "gzip, deflate"
    request.content_type = "application/octet-stream"
    response = object_storage.create_multipart_upload(namespace, bucket, request)

    assert response.status == 200
    print(response.headers)
    print(response.data)
    print(response.data.upload_id)

    response = object_storage.abort_multipart_upload(namespace,
                                                     bucket,
                                                     "test_multipart_file",
                                                     response.data.upload_id)

    assert response.status == 204


def test_multipart_upload_crud(object_storage, bucket):
    object_name = "test_multipart_file"

    # Create
    namespace = object_storage.get_namespace().data
    request = oraclebmc.object_storage.models.CreateMultipartUploadDetails()
    request.object = object_name
    request.content_encoding = "gzip, deflate"
    request.content_type = "application/octet-stream"
    response = object_storage.create_multipart_upload(namespace, bucket, request)

    assert response.status == 200

    upload_id = response.data.upload_id

    # Upload some parts
    test_data = 'This is a test {0}!\n\r'
    etags = []
    contents = ''
    for i in range(1, 4):
        part = test_data.format(i)
        response = object_storage.upload_part(namespace, bucket, object_name, upload_id, i, part)
        assert response.status == 200
        etags.append({"part_num": i, "etag": response.headers['etag']})
        contents += part

    response = object_storage.list_multipart_upload_parts(namespace, bucket, object_name, upload_id)
    assert response.status == 200
    assert 3 == len(response.data)

    # Prepare to commit the upload
    manifest = oraclebmc.object_storage.models.CommitMultipartUploadDetails()

    # Parts to exclude
    manifest.parts_to_exclude = []

    # Parts to commit
    parts_to_commit = []
    for etag in etags:
        detail = oraclebmc.object_storage.models.CommitMultipartUploadPartDetails()
        detail.etag = etag["etag"]
        detail.part_num = etag["part_num"]
        parts_to_commit.append(detail)
    manifest.parts_to_commit = parts_to_commit

    # Commit the multipart upload
    response = object_storage.commit_multipart_upload(namespace, bucket, object_name, upload_id, manifest)
    assert response.status == 200

    # Check that the remote object equals the parts uploaded.
    response = object_storage.get_object(namespace, bucket, object_name)
    assert response.status == 200
    object_contents = response.data.content.decode('UTF-8')
    assert contents == object_contents
    print(response.data.content.decode('UTF-8'))

    # Delete the upload.  This isn't needed for clean up since the bucket fixture will take care of
    # cleanup, but it tests the API.
    response = object_storage.delete_object(namespace, bucket, object_name)
    assert response.status == 204
