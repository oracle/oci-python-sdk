from tests.service_test_base import ServiceTestBase
import oraclebmc
import tests.util

class TestObjectStorage(ServiceTestBase):
    """Tests the operations of the ObjectStorageApi."""

    def test_get_namespace(self):
        response = self.context.object_storage_api.get_namespace()
        self.assertEqual(200, response.status)

    def test_bucket_CRUD(self):
        bucket_name = tests.util.unique_name('test_bucket')
        namespace = self.context.object_storage_api.get_namespace().data
        bucket_count = len(self.context.object_storage_api.list_buckets(namespace, self.context.config.tenancy, limit=100).data)

        # Create
        request = oraclebmc.models.CreateBucketDetails()
        request.name = bucket_name
        request.compartment_id = self.context.config.tenancy
        request.metadata = {'some key': 'some example metadata'}
        response = self.context.object_storage_api.create_bucket(namespace, request)

        self.assertEqual(200, response.status)
        bucket = response.data
        assert (type(bucket) is oraclebmc.models.Bucket)
        self.assertEqual(bucket_name, bucket.name)
        self.assertEqual('some example metadata', bucket.metadata['some key'])

        # Get
        response = self.context.object_storage_api.get_bucket(namespace, bucket_name)
        self.assertEqual(200, response.status)
        assert (type(response.data) is oraclebmc.models.Bucket)
        self.assertEqual(bucket_name, response.data.name)

        # List
        response = self.context.object_storage_api.list_buckets(namespace, self.context.config.tenancy, limit=100)
        self.assertEqual(200, response.status)
        self.assertEqual(bucket_count + 1, len(response.data))
        assert (type(response.data[0]) is oraclebmc.models.Bucket)

        # Update
        request = oraclebmc.models.UpdateBucketDetails()
        request.name = bucket_name
        request.metadata = {'new key': 'updated!', 'key2': 'another value'}
        response = self.context.object_storage_api.update_bucket(namespace, bucket_name, request)
        bucket = response.data
        self.assertEqual(200, response.status)
        assert (type(bucket) is oraclebmc.models.Bucket)
        self.assertEqual('another value', bucket.metadata['key2'])

        # Delete
        response = self.context.object_storage_api.delete_bucket(namespace, bucket_name)
        self.assertEqual(204, response.status)

    def test_object_CRUD(self):
        # Setup a bucket to use.
        object_name_A = 'object_A'
        bucket_name = tests.util.unique_name('test_object_CRUD')
        test_data = 'This is a test ' + tests.util.random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''
        namespace = self.context.object_storage_api.get_namespace().data

        request = oraclebmc.models.CreateBucketDetails()
        request.name = bucket_name
        request.compartment_id = self.context.config.tenancy
        response = self.context.object_storage_api.create_bucket(namespace, request)
        self.assertEqual(200, response.status)

        # Put an object
        response = self.context.object_storage_api.put_object(namespace, bucket_name, object_name_A, test_data)
        self.assertEqual(200, response.status)

        # Get it back
        response = self.context.object_storage_api.get_object(namespace, bucket_name, object_name_A)
        self.assertEqual(200, response.status)
        response_text = response.data.content.decode('UTF-8')
        self.assertEqual(len(test_data), len(response_text))
        self.assertEqual(test_data, response_text)
        assert (type(response.data) is oraclebmc.DataStream)

        # Head
        response = self.context.object_storage_api.head_object(namespace, bucket_name, object_name_A)
        self.assertEqual(200, response.status)
        assert (len(test_data) == int(response.headers['content-length']))

        # Put a couple more objects
        self.context.object_storage_api.put_object(namespace, bucket_name, 'second_object', tests.util.random_number_string())
        self.context.object_storage_api.put_object(namespace, bucket_name, 'third_object', tests.util.random_number_string())

        # List
        response = self.context.object_storage_api.list_objects(namespace, bucket_name)
        self.assertEqual(200, response.status)
        object_list = response.data
        assert (type(object_list) is oraclebmc.models.ListObjects)
        self.assertEqual(3, len(object_list.objects))
        assert (type(object_list.objects[0]) is oraclebmc.models.ObjectSummary)

        # Delete
        for summary in object_list.objects:
            response = self.context.object_storage_api.delete_object(namespace, bucket_name, summary.name)
            self.assertEqual(204, response.status)

        # Clean up
        response = self.context.object_storage_api.delete_bucket(namespace, bucket_name)
        self.assertEqual(204, response.status)

    def test_bucket_not_found(self):
        namespace = self.context.object_storage_api.get_namespace().data

        with self.assertRaises(oraclebmc.exceptions.ServiceError) as errorContext:
            self.context.object_storage_api.get_bucket(namespace, tests.util.unique_name('does_not_exist'))

        self.assertEqual(404, errorContext.exception.status)
        assert (type(errorContext.exception.data) is oraclebmc.models.Error)

    def test_get_bucket(self):
        namespace = self.context.object_storage_api.get_namespace().data
        response = self.context.object_storage_api.get_bucket(namespace, 'ReadOnlyTestBucket1')
        self.assertEqual(200, response.status)
        assert (type(response.data) is oraclebmc.models.Bucket)
        self.assertIsNotNone(response.data.metadata)
        self.assertEqual(0, len(response.data.metadata))

    def test_get_bucket_with_metadata(self):
        namespace = self.context.object_storage_api.get_namespace().data
        response = self.context.object_storage_api.get_bucket(namespace, 'ReadOnlyTestBucket5')
        self.assertEqual(200, response.status)
        assert (type(response.data) is oraclebmc.models.Bucket)
        self.assertIsNotNone(response.data.metadata)
        self.assertEqual('bar1', response.data.metadata['foo1'])
        self.assertEqual('bar2', response.data.metadata['foo2'])

    def test_list_buckets(self):
        namespace = self.context.object_storage_api.get_namespace().data
        response = self.context.object_storage_api.list_buckets(namespace, self.context.config.tenancy)
        self.assertEqual(200, response.status)
        assert (len(response.data) > 0)
        assert (type(response.data[0]) is oraclebmc.models.Bucket)

    def test_list_buckets_truncated(self):
        namespace = self.context.object_storage_api.get_namespace().data
        response = self.context.object_storage_api.list_buckets(namespace, self.context.config.tenancy, limit=2)
        self.assertEqual(200, response.status)
        self.assertEqual(2, len(response.data))
        assert (type(response.data[0]) is oraclebmc.models.Bucket)
        assert (response.has_next_page)
        first_bucket_name = response.data[0].name

        response = self.context.object_storage_api.list_buckets(namespace, self.context.config.tenancy, limit=2, page=response.next_page)
        self.assertEqual(200, response.status)
        self.assertEqual(2, len(response.data))
        self.assertNotEqual(first_bucket_name, response.data[0].name)

    def test_get_object(self):
        namespace = self.context.object_storage_api.get_namespace().data
        response = self.context.object_storage_api.get_object(namespace, 'ReadOnlyTestBucket1', 'object1')
        self.assertEqual(200, response.status)
        assert (type(response.data) is oraclebmc.DataStream)

    # TODO: metadata is not yet hooked up
    def DISABLE_test_get_object_with_user_metadata(self):
        namespace = self.context.object_storage_api.get_namespace().data
        response = self.context.object_storage_api.get_object(namespace, 'ReadOnlyTestBucket4', 'hasUserMetadata.json')
        self.assertEqual(200, response.status)
        assert (type(response.data) is oraclebmc.DataStream)
        self.assertEqual('bar1', response.headers['opc-meta-foo1'])
        self.assertEqual('bar2', response.headers['opc-meta-foo2'])

    def test_list_objects(self):
        namespace = self.context.object_storage_api.get_namespace().data
        response = self.context.object_storage_api.list_objects(namespace, 'ReadOnlyTestBucket1')
        self.assertEqual(200, response.status)
        assert (type(response.data) is oraclebmc.models.ListObjects)
        self.assertEqual(5, len(response.data.objects))
        self.assertIsNone(response.data.prefixes)

    def test_list_objects_empty_bucket(self):
        namespace = self.context.object_storage_api.get_namespace().data
        response = self.context.object_storage_api.list_objects(namespace, 'ReadOnlyTestBucket5')
        self.assertEqual(200, response.status)
        assert (type(response.data) is oraclebmc.models.ListObjects)
        self.assertEqual(0, len(response.data.objects))
        self.assertIsNone(response.data.prefixes)

    def test_list_objects_with_prefix_and_delimiter(self):
        namespace = self.context.object_storage_api.get_namespace().data
        response = self.context.object_storage_api.list_objects(namespace, 'ReadOnlyTestBucket2', prefix='a/b/', delimiter='/')
        self.assertEqual(200, response.status)
        assert (type(response.data) is oraclebmc.models.ListObjects)
        self.assertEqual(2, len(response.data.objects))
        self.assertEqual(1, len(response.data.prefixes))
        self.assertIsNone(response.data.next_start_with)

    def test_list_objects_truncated(self):
        namespace = self.context.object_storage_api.get_namespace().data
        response = self.context.object_storage_api.list_objects(namespace, 'ReadOnlyTestBucket1', limit=3)
        self.assertEqual(200, response.status)
        assert (type(response.data) is oraclebmc.models.ListObjects)
        self.assertEqual(3, len(response.data.objects))
        self.assertIsNone(response.data.prefixes)
        self.assertIsNotNone(response.data.next_start_with)
        first_object_name = response.data.objects[0].name

        response = self.context.object_storage_api.list_objects(namespace, 'ReadOnlyTestBucket1', start=response.data.next_start_with)
        self.assertEqual(2, len(response.data.objects))
        self.assertIsNone(response.data.prefixes)
        self.assertIsNone(response.data.next_start_with)
        self.assertNotEqual(first_object_name, response.data.objects[0].name)


    def test_head_object(self):
        namespace = self.context.object_storage_api.get_namespace().data
        response = self.context.object_storage_api.head_object(namespace, 'ReadOnlyTestBucket4', 'hasUserMetadata.json')
        self.assertEqual(200, response.status)
        self.assertIsNone (response.data)

        # TODO: metadata is not yet hooked up
        # self.assertEqual('bar1', response.headers['opc-meta-foo1'])
        # self.assertEqual('bar2', response.headers['opc-meta-foo2'])

if __name__ == '__main__':
    unittest.main()