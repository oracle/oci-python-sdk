from tests.service_test_base import ServiceTestBase
import oraclebmc
import tests.util
import time


class TestStreaming(ServiceTestBase):
    """Tests streaming of various types to and from the ObjectStorageApi."""
    def setUp(self):
        self.config = self.create_config()
        self.api = oraclebmc.apis.ObjectStorageApi(self.config)

        self.bucket_name = tests.util.unique_name('test_python_streaming')
        self.namespace = self.api.get_namespace().data

        request = oraclebmc.models.CreateBucketDetails()
        request.name = self.bucket_name
        request.compartment_id = self.config.tenancy
        response = self.api.create_bucket(self.namespace, request)
        assert response.status == 200

    def tearDown(self):
        # Delete new objects and bucket
        try:
            object_list = self.api.list_objects(self.namespace, self.bucket_name).data

            for summary in object_list.objects:
                response = self.api.delete_object(self.namespace, self.bucket_name, summary.name)
                assert response.status == 200
        except:
            print('TearDown: Could not delete new objects.')

        try:
            self.api.delete_bucket(self.namespace, self.bucket_name)
        except:
            print('TearDown: Could not delete new bucket.')

    def test_string_object(self):
        name = 'string_1'
        body = 'This is a test string.'
        response = self.api.put_object(self.namespace, self.bucket_name, name, body)
        assert response.status == 200

        response = self.api.get_object(self.namespace, self.bucket_name, name)
        assert response.status == 200
        assert body == response.data.content.decode('UTF-8')

    def test_text_file_streaming(self):
        name = 'text_file'
        test_file = tests.util.get_resource_path('config')

        # Put an object
        with open(test_file, 'r') as file:
            response = self.api.put_object(self.namespace, self.bucket_name, name, file)
        assert response.status == 200

        # Get it back
        response = self.api.get_object(self.namespace, self.bucket_name, name)
        assert response.status == 200

        # Stream the file into memory
        response_text = ''
        chunk_count = 0
        for chunk in response.data.iter_content(chunk_size=5):
            text = chunk.decode('UTF-8')
            response_text += text
            chunk_count += 1

        assert (chunk_count > 1)

        # Check content against the original file
        with open(test_file, 'r') as file:
            file_content = file.read()
            assert file_content == response_text

        # Head
        response = self.api.head_object(self.namespace, self.bucket_name, name)
        assert response.status == 200
        assert len(file_content) == int(response.headers['content-length'])

    def test_binary_file_streaming(self):
        name = 'image_file'
        test_file = tests.util.get_resource_path('test_image.png')

        # Put an object
        with open(test_file, 'rb') as file:
            response = self.api.put_object(self.namespace, self.bucket_name, name, file)
        assert response.status == 200

        # Get it back
        response = self.api.get_object(self.namespace, self.bucket_name, name)
        assert response.status == 200

        # Stream the file into memory
        response_data = b''
        chunk_count = 0
        for chunk in response.data.iter_content(chunk_size=10):
            text = chunk
            response_data += text
            chunk_count += 1

        assert (chunk_count > 1)

        # Check content against the original file
        with open(test_file, 'rb') as file:
            file_content = file.read()
            assert file_content == response_data

        # Head
        response = self.api.head_object(self.namespace, self.bucket_name, name)
        assert response.status == 200
        assert len(file_content) == int(response.headers['content-length'])

    def test_invalid_object_types(self):
        with self.assertRaises(TypeError):
            self.api.put_object(self.namespace, self.bucket_name, 'an_int', 24601)

        with self.assertRaises(TypeError):
            self.api.put_object(self.namespace, self.bucket_name, 'a_time', time.time())

        with self.assertRaises(TypeError):
            self.api.put_object(
                self.namespace,
                self.bucket_name,
                'a_user',
                oraclebmc.models.User()
            )

    def test_object_not_found(self):
        with self.assertRaises(oraclebmc.exceptions.ServiceError) as errorContext:
            self.api.get_object(self.namespace, self.bucket_name, 'does_not_exist')

        assert errorContext.exception.status == 404
        assert type(errorContext.exception.data) is oraclebmc.models.Error
