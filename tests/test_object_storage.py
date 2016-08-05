from tests.service_test_base import ServiceTestBase
import oraclebmi
import tests.util
import resource

class TestObjectStorage(ServiceTestBase):
    """Tests the operations of the ObjectStorageApi."""

    def test_get_namespace(self):
        response = self.context.object_storage_api.get_namespace()
        self.assertEqual(200, response.status)

    def test_bucket_CRUD(self):
        bucket_name = tests.util.unique_name('test_bucket')
        namespace = self.context.object_storage_api.get_namespace().data
        bucket_count = len(self.context.object_storage_api.list_buckets(namespace, limit=100).data)

        # Create
        request = oraclebmi.models.CreateBucket()
        request.name = bucket_name
        request.metadata = {'some key': 'some example metadata'}
        response = self.context.object_storage_api.create_bucket(namespace, request)

        self.assertEqual(200, response.status)
        bucket = response.data
        assert (type(bucket) is oraclebmi.models.Bucket)
        self.assertEqual(bucket_name, bucket.name)
        self.assertEqual('some example metadata', bucket.metadata['some key'])

        # Get
        response = self.context.object_storage_api.get_bucket(namespace, bucket_name)
        self.assertEqual(200, response.status)
        assert (type(response.data) is oraclebmi.models.Bucket)
        self.assertEqual(bucket_name, response.data.name)

        # List
        response = self.context.object_storage_api.list_buckets(namespace, limit=100)
        self.assertEqual(200, response.status)
        self.assertEqual(bucket_count + 1, len(response.data))
        assert (type(response.data[0]) is oraclebmi.models.Bucket)

        # Update
        request = oraclebmi.models.UpdateBucket()
        request.name = bucket_name
        request.metadata = {'new key': 'updated!', 'key2': 'another value'}
        response = self.context.object_storage_api.update_bucket(namespace, bucket_name, request)
        bucket = response.data
        self.assertEqual(200, response.status)
        assert (type(bucket) is oraclebmi.models.Bucket)
        self.assertEqual('another value', bucket.metadata['key2'])

        # Delete
        response = self.context.object_storage_api.delete_bucket(namespace, bucket_name)
        self.assertEqual(200, response.status)

    def test_object_CRUD(self):
        # Setup a bucket to use.
        object_name_A = 'object_A'
        bucket_name = tests.util.unique_name('test_object_CRUD')
        test_data = 'This is a test ' + tests.util.random_number_string() + '!/n/r/\/~%s;"/,{}><+=:.*)('''
        namespace = self.context.object_storage_api.get_namespace().data

        request = oraclebmi.models.CreateBucket()
        request.name = bucket_name
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
        assert (type(response.data) is oraclebmi.DataStream)

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
        assert (type(object_list) is oraclebmi.models.ListObjects)
        self.assertEqual(3, len(object_list.objects))
        assert (type(object_list.objects[0]) is oraclebmi.models.ObjectSummary)

        # Delete
        for summary in object_list.objects:
            response = self.context.object_storage_api.delete_object(namespace, bucket_name, summary.name)
            self.assertEqual(200, response.status)

        # Clean up
        response = self.context.object_storage_api.delete_bucket(namespace, bucket_name)
        self.assertEqual(200, response.status)

    def test_bucket_not_found(self):
        namespace = self.context.object_storage_api.get_namespace().data

        with self.assertRaises(oraclebmi.exceptions.ServiceError) as errorContext:
            self.context.object_storage_api.get_bucket(namespace, tests.util.unique_name('does_not_exist'))

        self.assertEqual(404, errorContext.exception.status)
        assert (type(errorContext.exception.data) is oraclebmi.models.Error)

if __name__ == '__main__':
    unittest.main()