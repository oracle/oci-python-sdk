from tests.service_test_base import ServiceTestBase
import oraclebmc
import tests.util
import time

class TestStreaming(ServiceTestBase):
    """Tests streaming of various types to and from the ObjectStorageApi."""

    def setUp(self):
        self.context = self.create_context()

        self.bucket_name = tests.util.unique_name('test_python_streaming')
        self.namespace = self.context.object_storage_api.get_namespace().data

        request = oraclebmc.models.CreateBucketDetails()
        request.name = self.bucket_name
        request.compartment_id = self.context.config.tenancy
        response = self.context.object_storage_api.create_bucket(self.namespace, request)
        self.assertEqual(200, response.status)

    def tearDown(self):
        # Delete new objects and bucket
        try:
            object_list = self.context.object_storage_api.list_objects(self.namespace, self.bucket_name).data

            for summary in object_list.objects:
                response = self.context.object_storage_api.delete_object(self.namespace, self.bucket_name, summary.name)
                self.assertEqual(200, response.status)
        except:
            print('TearDown: Could not delete new objects.')

        try:
            self.context.object_storage_api.delete_bucket(self.namespace, self.bucket_name)
        except:
            print('TearDown: Could not delete new bucket.')

    def test_string_object(self):
        name = 'string_1'
        body = 'This is a test string.'
        response = self.context.object_storage_api.put_object(self.namespace, self.bucket_name, name, body)
        self.assertEqual(200, response.status)

        response = self.context.object_storage_api.get_object(self.namespace, self.bucket_name, name)
        self.assertEqual(200, response.status)
        self.assertEqual(body, response.data.content.decode('UTF-8'))

    def test_text_file_streaming(self):
        name = 'text_file'
        test_file = tests.util.get_resource_path('config')

        # Put an object
        with open(test_file, 'r') as file:
            response = self.context.object_storage_api.put_object(self.namespace, self.bucket_name, name, file)
        self.assertEqual(200, response.status)

        # Get it back
        response = self.context.object_storage_api.get_object(self.namespace, self.bucket_name, name)
        self.assertEqual(200, response.status)

        # Stream the file into memory
        response_text = ''
        chunk_count = 0;
        for chunk in response.data.iter_content(chunk_size=5):
            text = chunk.decode('UTF-8')
            response_text += text
            chunk_count += 1

        assert (chunk_count > 1)

        # Check content against the original file
        file_content = None
        with open(test_file, 'r') as file:
            file_content = file.read()
            self.assertEquals(file_content, response_text)

        # Head
        response = self.context.object_storage_api.head_object(self.namespace, self.bucket_name, name)
        self.assertEqual(200, response.status)
        assert (len(file_content) == int(response.headers['content-length']))

    def test_binary_file_streaming(self):
        name = 'image_file'
        test_file = tests.util.get_resource_path('test_image.png')

        # Put an object
        with open(test_file, 'rb') as file:
            response = self.context.object_storage_api.put_object(self.namespace, self.bucket_name, name, file)
        self.assertEqual(200, response.status)

        # Get it back
        response = self.context.object_storage_api.get_object(self.namespace, self.bucket_name, name)
        self.assertEqual(200, response.status)

        # Stream the file into memory
        response_data = b''
        chunk_count = 0;
        for chunk in response.data.iter_content(chunk_size=10):
            text = chunk
            response_data += text
            chunk_count += 1

        assert (chunk_count > 1)

        # Check content against the original file
        file_content = None
        with open(test_file, 'rb') as file:
            file_content = file.read()
            self.assertEquals(file_content, response_data)

        # Head
        response = self.context.object_storage_api.head_object(self.namespace, self.bucket_name, name)
        self.assertEqual(200, response.status)
        assert (len(file_content) == int(response.headers['content-length']))

    def test_invalid_object_types(self):
        with self.assertRaises(TypeError):
            self.context.object_storage_api.put_object(self.namespace, self.bucket_name, 'an_int', 24601)

        with self.assertRaises(TypeError):
            self.context.object_storage_api.put_object(self.namespace, self.bucket_name, 'a_time', time.time())

        with self.assertRaises(TypeError):
            self.context.object_storage_api.put_object(self.namespace, self.bucket_name, 'a_user', oraclebmc.models.User())


    def test_object_not_found(self):
        with self.assertRaises(oraclebmc.exceptions.ServiceError) as errorContext:
            self.context.object_storage_api.get_object(self.namespace, self.bucket_name, 'does_not_exist')

        self.assertEqual(404, errorContext.exception.status)
        assert (type(errorContext.exception.data) is oraclebmc.models.Error)

if __name__ == '__main__':
    unittest.main()