from tests.util import get_resource_path, random_number_string, unique_name
import oraclebmc
import pytest


def test_get_namespace(object_storage):
    response = object_storage.get_namespace()
    assert response.status == 200


def test_bucket_crud(object_storage, config):
    bucket_name = unique_name('test_bucket')
    namespace = object_storage.get_namespace().data
    bucket_count = len(object_storage.list_buckets(namespace, config.tenancy, limit=100).data)

    # Create
    request = oraclebmc.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = config.tenancy
    request.metadata = {'some key': 'some example metadata'}
    response = object_storage.create_bucket(namespace, request)
    assert response.status == 200

    bucket = response.data
    assert type(bucket) is oraclebmc.models.Bucket
    assert bucket_name == bucket.name
    assert 'some example metadata' == bucket.metadata['some key']

    # Get
    response = object_storage.get_bucket(namespace, bucket_name)
    assert response.status == 200
    assert type(response.data) is oraclebmc.models.Bucket
    assert bucket_name == response.data.name

    # List
    response = object_storage.list_buckets(namespace, config.tenancy, limit=100)
    assert response.status == 200
    assert bucket_count + 1 == len(response.data)
    assert type(response.data[0]) is oraclebmc.models.Bucket

    # Update
    request = oraclebmc.models.UpdateBucketDetails()
    request.name = bucket_name
    request.metadata = {'new key': 'updated!', 'key2': 'another value'}
    response = object_storage.update_bucket(namespace, bucket_name, request)
    bucket = response.data
    assert response.status == 200
    assert type(bucket) is oraclebmc.models.Bucket
    assert 'another value' == bucket.metadata['key2']

    # Delete
    response = object_storage.delete_bucket(namespace, bucket_name)
    assert response.status == 204


def test_object_crud(object_storage, config):
    # Setup a bucket to use.
    object_name_a = 'object_A'
    bucket_name = unique_name('test_object_CRUD')
    test_data = 'This is a test ' + random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''
    namespace = object_storage.get_namespace().data

    request = oraclebmc.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = config.tenancy
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
    assert type(response.data) is oraclebmc.DataStream

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
    assert type(object_list) is oraclebmc.models.ListObjects
    assert 3 == len(object_list.objects)
    assert type(object_list.objects[0]) is oraclebmc.models.ObjectSummary

    # Delete
    for summary in object_list.objects:
        response = object_storage.delete_object(namespace, bucket_name, summary.name)
        assert response.status == 204

    # Clean up
    response = object_storage.delete_bucket(namespace, bucket_name)
    assert response.status == 204


def test_object_crud_with_metadata(object_storage, config):
    # Setup a bucket to use.
    object_name_a = 'object_A'
    bucket_name = unique_name('test_object_CRUD_with_metadata')
    test_data = 'This is a test ' + random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''
    namespace = object_storage.get_namespace().data

    request = oraclebmc.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = config.tenancy
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
    assert type(response.data) is oraclebmc.DataStream
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


def test_put_empty_file(object_storage, config):
    # Setup a bucket to use.
    object_name = 'empty_object'
    bucket_name = unique_name('test_object_CRUD')
    namespace = object_storage.get_namespace().data
    test_file = get_resource_path('empty_file')

    request = oraclebmc.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = config.tenancy
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


def test_put_empty_string(object_storage, config):
    # Setup a bucket to use.
    object_name = 'empty_object'
    bucket_name = unique_name('test_object_CRUD')
    namespace = object_storage.get_namespace().data

    request = oraclebmc.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = config.tenancy
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


def test_bucket_not_found(object_storage):
    namespace = object_storage.get_namespace().data

    with pytest.raises(oraclebmc.exceptions.ServiceError) as excinfo:
        object_storage.get_bucket(namespace, unique_name('does_not_exist'))

    assert excinfo.value.status == 404


def test_get_bucket(object_storage):
    namespace = object_storage.get_namespace().data
    response = object_storage.get_bucket(namespace, 'ReadOnlyTestBucket1')
    assert response.status == 200
    assert type(response.data) is oraclebmc.models.Bucket
    assert response.data.metadata is not None
    assert 0 == len(response.data.metadata)


def test_get_bucket_with_metadata(object_storage):
    namespace = object_storage.get_namespace().data
    response = object_storage.get_bucket(namespace, 'ReadOnlyTestBucket5')
    assert response.status == 200
    assert type(response.data) is oraclebmc.models.Bucket
    assert response.data.metadata is not None
    assert 'bar1' == response.data.metadata['foo1']
    assert 'bar2' == response.data.metadata['foo2']


def test_list_buckets(object_storage, config):
    namespace = object_storage.get_namespace().data
    response = object_storage.list_buckets(namespace, config.tenancy)
    assert response.status == 200
    assert len(response.data) > 0
    assert type(response.data[0]) is oraclebmc.models.Bucket


def test_list_buckets_truncated(object_storage, config):
    namespace = object_storage.get_namespace().data
    response = object_storage.list_buckets(namespace, config.tenancy, limit=2)
    assert response.status == 200
    assert 2 == len(response.data)
    assert type(response.data[0]) is oraclebmc.models.Bucket
    assert response.has_next_page
    first_bucket_name = response.data[0].name

    response = object_storage.list_buckets(
        namespace, config.tenancy, limit=2, page=response.next_page)
    assert response.status == 200
    assert 2 == len(response.data)
    assert first_bucket_name != response.data[0].name


def test_get_object(object_storage):
    namespace = object_storage.get_namespace().data
    response = object_storage.get_object(namespace, 'ReadOnlyTestBucket1', 'object1')
    assert response.status == 200
    assert type(response.data) is oraclebmc.DataStream


def test_get_object_with_user_metadata(object_storage):
    namespace = object_storage.get_namespace().data
    response = object_storage.get_object(namespace, 'ReadOnlyTestBucket4', 'hasUserMetadata.json')
    assert response.status == 200
    assert type(response.data) is oraclebmc.DataStream
    assert 'bar1' == response.headers['opc-meta-foo1']
    assert 'bar2' == response.headers['opc-meta-foo2']


def test_list_objects(object_storage):
    namespace = object_storage.get_namespace().data
    response = object_storage.list_objects(namespace, 'ReadOnlyTestBucket1')
    assert response.status == 200
    assert type(response.data) is oraclebmc.models.ListObjects
    assert 5 == len(response.data.objects)
    assert response.data.prefixes is None


def test_list_objects_empty_bucket(object_storage):
    namespace = object_storage.get_namespace().data
    response = object_storage.list_objects(namespace, 'ReadOnlyTestBucket5')
    assert response.status == 200
    assert type(response.data) is oraclebmc.models.ListObjects
    assert 0 == len(response.data.objects)
    assert response.data.prefixes is None


def test_list_objects_with_prefix_and_delimiter(object_storage):
    namespace = object_storage.get_namespace().data
    response = object_storage.list_objects(
        namespace, 'ReadOnlyTestBucket2', prefix='a/b/', delimiter='/')
    assert response.status == 200
    assert type(response.data) is oraclebmc.models.ListObjects
    assert 2 == len(response.data.objects)
    assert 1 == len(response.data.prefixes)
    assert response.data.next_start_with is None


def test_list_objects_truncated(object_storage):
    namespace = object_storage.get_namespace().data
    response = object_storage.list_objects(namespace, 'ReadOnlyTestBucket1', limit=3)
    assert response.status == 200
    assert type(response.data) is oraclebmc.models.ListObjects
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


def test_head_object(object_storage):
    namespace = object_storage.get_namespace().data
    response = object_storage.head_object(namespace, 'ReadOnlyTestBucket4', 'hasUserMetadata.json')
    assert response.status == 200
    assert response.data is None
    assert 'bar1' == response.headers['opc-meta-foo1']
    assert 'bar2' == response.headers['opc-meta-foo2']


def test_head_not_found(object_storage):
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
