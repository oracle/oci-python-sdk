from tests.service_test_base import ServiceTestBase
from tests.util import get_resource_path, random_number_string, unique_name
import oraclebmc


class TestObjectStorage(ServiceTestBase):
    """Tests the operations of the ObjectStorageApi."""

    def setUp(self):
        self.config = self.create_config()
        self.api = oraclebmc.apis.ObjectStorageApi(self.config)

    def test_get_namespace(self):
        response = self.api.get_namespace()
        self.assertEqual(200, response.status)

    def test_bucket_CRUD(self):
        bucket_name = unique_name('test_bucket')
        namespace = self.api.get_namespace().data
        bucket_count = len(self.api.list_buckets(namespace, self.config.tenancy, limit=100).data)

        # Create
        request = oraclebmc.models.CreateBucketDetails()
        request.name = bucket_name
        request.compartment_id = self.config.tenancy
        request.metadata = {'some key': 'some example metadata'}
        response = self.api.create_bucket(namespace, request)

        self.assertEqual(200, response.status)
        bucket = response.data
        assert type(bucket) is oraclebmc.models.Bucket
        self.assertEqual(bucket_name, bucket.name)
        self.assertEqual('some example metadata', bucket.metadata['some key'])

        # Get
        response = self.api.get_bucket(namespace, bucket_name)
        self.assertEqual(200, response.status)
        assert type(response.data) is oraclebmc.models.Bucket
        self.assertEqual(bucket_name, response.data.name)

        # List
        response = self.api.list_buckets(namespace, self.config.tenancy, limit=100)
        self.assertEqual(200, response.status)
        self.assertEqual(bucket_count + 1, len(response.data))
        assert type(response.data[0]) is oraclebmc.models.Bucket

        # Update
        request = oraclebmc.models.UpdateBucketDetails()
        request.name = bucket_name
        request.metadata = {'new key': 'updated!', 'key2': 'another value'}
        response = self.api.update_bucket(namespace, bucket_name, request)
        bucket = response.data
        self.assertEqual(200, response.status)
        assert type(bucket) is oraclebmc.models.Bucket
        self.assertEqual('another value', bucket.metadata['key2'])

        # Delete
        response = self.api.delete_bucket(namespace, bucket_name)
        self.assertEqual(204, response.status)

    def test_object_CRUD(self):
        # Setup a bucket to use.
        object_name_a = 'object_A'
        bucket_name = unique_name('test_object_CRUD')
        test_data = 'This is a test ' + random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''
        namespace = self.api.get_namespace().data

        request = oraclebmc.models.CreateBucketDetails()
        request.name = bucket_name
        request.compartment_id = self.config.tenancy
        response = self.api.create_bucket(namespace, request)
        self.assertEqual(200, response.status)

        # Put an object
        response = self.api.put_object(namespace, bucket_name, object_name_a, test_data)
        self.assertEqual(200, response.status)

        # Get it back
        response = self.api.get_object(namespace, bucket_name, object_name_a)
        self.assertEqual(200, response.status)
        response_text = response.data.content.decode('UTF-8')
        self.assertEqual(len(test_data), len(response_text))
        self.assertEqual(test_data, response_text)
        assert type(response.data) is oraclebmc.DataStream

        # Head
        response = self.api.head_object(namespace, bucket_name, object_name_a)
        self.assertEqual(200, response.status)
        assert len(test_data) == int(response.headers['content-length'])

        # Put a couple more objects
        self.api.put_object(
            namespace, bucket_name, 'second_object', random_number_string())
        self.api.put_object(
            namespace, bucket_name, 'third_object', random_number_string())

        # List
        response = self.api.list_objects(namespace, bucket_name)
        self.assertEqual(200, response.status)
        object_list = response.data
        assert type(object_list) is oraclebmc.models.ListObjects
        self.assertEqual(3, len(object_list.objects))
        assert type(object_list.objects[0]) is oraclebmc.models.ObjectSummary

        # Delete
        for summary in object_list.objects:
            response = self.api.delete_object(namespace, bucket_name, summary.name)
            self.assertEqual(204, response.status)

        # Clean up
        response = self.api.delete_bucket(namespace, bucket_name)
        self.assertEqual(204, response.status)

    def test_object_CRUD_with_metadata(self):
        # Setup a bucket to use.
        object_name_a = 'object_A'
        bucket_name = unique_name('test_object_CRUD_with_metadata')
        test_data = 'This is a test ' + random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''
        namespace = self.api.get_namespace().data

        request = oraclebmc.models.CreateBucketDetails()
        request.name = bucket_name
        request.compartment_id = self.config.tenancy
        response = self.api.create_bucket(namespace, request)
        self.assertEqual(200, response.status)

        # Put an object
        response = self.api.put_object(
            namespace, bucket_name, object_name_a, test_data,
            opc_meta={'foo1': 'bar1', 'foo2': 'bar2'})
        self.assertEqual(200, response.status)

        # Get it back
        response = self.api.get_object(namespace, bucket_name, object_name_a)
        self.assertEqual(200, response.status)
        response_text = response.data.content.decode('UTF-8')
        self.assertEqual(len(test_data), len(response_text))
        self.assertEqual(test_data, response_text)
        assert type(response.data) is oraclebmc.DataStream
        self.assertEqual('bar1', response.headers['opc-meta-foo1'])
        self.assertEqual('bar2', response.headers['opc-meta-foo2'])

        # Head
        response = self.api.head_object(namespace, bucket_name, object_name_a)
        self.assertEqual(200, response.status)
        assert len(test_data) == int(response.headers['content-length'])
        self.assertEqual('bar1', response.headers['opc-meta-foo1'])
        self.assertEqual('bar2', response.headers['opc-meta-foo2'])

        # Delete
        response = self.api.delete_object(namespace, bucket_name, object_name_a)
        self.assertEqual(204, response.status)

        # Clean up
        response = self.api.delete_bucket(namespace, bucket_name)
        self.assertEqual(204, response.status)

    def test_put_empty_file(self):
        # Setup a bucket to use.
        object_name = 'empty_object'
        bucket_name = unique_name('test_object_CRUD')
        namespace = self.api.get_namespace().data
        test_file = get_resource_path('empty_file')

        request = oraclebmc.models.CreateBucketDetails()
        request.name = bucket_name
        request.compartment_id = self.config.tenancy
        response = self.api.create_bucket(namespace, request)
        self.assertEqual(200, response.status)

        # Put empty file
        with open(test_file, 'rb') as file:
            response = self.api.put_object(namespace, bucket_name, object_name, file)
            self.assertEqual(200, response.status)

        # Get it back
        response = self.api.get_object(namespace, bucket_name, object_name)
        self.assertEqual(200, response.status)
        response_text = response.data.content.decode('UTF-8')
        self.assertEqual(0, len(response_text))

        # Head
        response = self.api.head_object(namespace, bucket_name, object_name)
        self.assertEqual(200, response.status)
        assert 0 == int(response.headers['content-length'])

        # Clean up
        response = self.api.delete_object(namespace, bucket_name, object_name)
        self.assertEqual(204, response.status)
        response = self.api.delete_bucket(namespace, bucket_name)
        self.assertEqual(204, response.status)

    def test_put_empty_string(self):
        # Setup a bucket to use.
        object_name = 'empty_object'
        bucket_name = unique_name('test_object_CRUD')
        namespace = self.api.get_namespace().data

        request = oraclebmc.models.CreateBucketDetails()
        request.name = bucket_name
        request.compartment_id = self.config.tenancy
        response = self.api.create_bucket(namespace, request)
        self.assertEqual(200, response.status)

        # Put empty string
        response = self.api.put_object(namespace, bucket_name, object_name, '')
        self.assertEqual(200, response.status)

        # Get it back
        response = self.api.get_object(namespace, bucket_name, object_name)
        self.assertEqual(200, response.status)
        response_text = response.data.content.decode('UTF-8')
        self.assertEqual(0, len(response_text))

        # Head
        response = self.api.head_object(namespace, bucket_name, object_name)
        self.assertEqual(200, response.status)
        assert 0 == int(response.headers['content-length'])

        # Clean up
        response = self.api.delete_object(namespace, bucket_name, object_name)
        self.assertEqual(204, response.status)
        response = self.api.delete_bucket(namespace, bucket_name)
        self.assertEqual(204, response.status)

    def test_bucket_not_found(self):
        namespace = self.api.get_namespace().data

        with self.assertRaises(oraclebmc.exceptions.ServiceError) as errorContext:
            self.api.get_bucket(namespace, unique_name('does_not_exist'))

        self.assertEqual(404, errorContext.exception.status)
        assert type(errorContext.exception.data) is oraclebmc.models.Error

    def test_get_bucket(self):
        namespace = self.api.get_namespace().data
        response = self.api.get_bucket(namespace, 'ReadOnlyTestBucket1')
        self.assertEqual(200, response.status)
        assert type(response.data) is oraclebmc.models.Bucket
        self.assertIsNotNone(response.data.metadata)
        self.assertEqual(0, len(response.data.metadata))

    def test_get_bucket_with_metadata(self):
        namespace = self.api.get_namespace().data
        response = self.api.get_bucket(namespace, 'ReadOnlyTestBucket5')
        self.assertEqual(200, response.status)
        assert type(response.data) is oraclebmc.models.Bucket
        self.assertIsNotNone(response.data.metadata)
        self.assertEqual('bar1', response.data.metadata['foo1'])
        self.assertEqual('bar2', response.data.metadata['foo2'])

    def test_list_buckets(self):
        namespace = self.api.get_namespace().data
        response = self.api.list_buckets(namespace, self.config.tenancy)
        self.assertEqual(200, response.status)
        assert len(response.data) > 0
        assert type(response.data[0]) is oraclebmc.models.Bucket

    def test_list_buckets_truncated(self):
        namespace = self.api.get_namespace().data
        response = self.api.list_buckets(namespace, self.config.tenancy, limit=2)
        self.assertEqual(200, response.status)
        self.assertEqual(2, len(response.data))
        assert type(response.data[0]) is oraclebmc.models.Bucket
        assert response.has_next_page
        first_bucket_name = response.data[0].name

        response = self.api.list_buckets(
            namespace, self.config.tenancy, limit=2, page=response.next_page)
        self.assertEqual(200, response.status)
        self.assertEqual(2, len(response.data))
        self.assertNotEqual(first_bucket_name, response.data[0].name)

    def test_get_object(self):
        namespace = self.api.get_namespace().data
        response = self.api.get_object(namespace, 'ReadOnlyTestBucket1', 'object1')
        self.assertEqual(200, response.status)
        assert type(response.data) is oraclebmc.DataStream

    def test_get_object_with_user_metadata(self):
        namespace = self.api.get_namespace().data
        response = self.api.get_object(namespace, 'ReadOnlyTestBucket4', 'hasUserMetadata.json')
        self.assertEqual(200, response.status)
        assert type(response.data) is oraclebmc.DataStream
        self.assertEqual('bar1', response.headers['opc-meta-foo1'])
        self.assertEqual('bar2', response.headers['opc-meta-foo2'])

    def test_list_objects(self):
        namespace = self.api.get_namespace().data
        response = self.api.list_objects(namespace, 'ReadOnlyTestBucket1')
        self.assertEqual(200, response.status)
        assert type(response.data) is oraclebmc.models.ListObjects
        self.assertEqual(5, len(response.data.objects))
        self.assertIsNone(response.data.prefixes)

    def test_list_objects_empty_bucket(self):
        namespace = self.api.get_namespace().data
        response = self.api.list_objects(namespace, 'ReadOnlyTestBucket5')
        self.assertEqual(200, response.status)
        assert type(response.data) is oraclebmc.models.ListObjects
        self.assertEqual(0, len(response.data.objects))
        self.assertIsNone(response.data.prefixes)

    def test_list_objects_with_prefix_and_delimiter(self):
        namespace = self.api.get_namespace().data
        response = self.api.list_objects(
            namespace, 'ReadOnlyTestBucket2', prefix='a/b/', delimiter='/')
        self.assertEqual(200, response.status)
        assert type(response.data) is oraclebmc.models.ListObjects
        self.assertEqual(2, len(response.data.objects))
        self.assertEqual(1, len(response.data.prefixes))
        self.assertIsNone(response.data.next_start_with)

    def test_list_objects_truncated(self):
        namespace = self.api.get_namespace().data
        response = self.api.list_objects(namespace, 'ReadOnlyTestBucket1', limit=3)
        assert response.status == 200
        assert type(response.data) is oraclebmc.models.ListObjects
        assert len(response.data.objects) == 3
        assert response.data.prefixes is None
        assert response.data.next_start_with is not None
        first_object_name = response.data.objects[0].name

        response = self.api.list_objects(
            namespace, 'ReadOnlyTestBucket1', start=response.data.next_start_with)
        self.assertEqual(2, len(response.data.objects))
        assert response.data.prefixes is None
        assert response.data.next_start_with is None
        assert first_object_name != response.data.objects[0].name

    def test_head_object(self):
        namespace = self.api.get_namespace().data
        response = self.api.head_object(namespace, 'ReadOnlyTestBucket4', 'hasUserMetadata.json')
        assert response.status == 200
        assert response.data is None

        assert 'bar1' == response.headers['opc-meta-foo1']
        assert 'bar2' == response.headers['opc-meta-foo2']
