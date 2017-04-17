import oraclebmc
import tests.util
import time
import pytest
from . import util


@pytest.fixture
def namespace(object_storage):
    return object_storage.get_namespace().data


@pytest.yield_fixture
def bucket_name(namespace, object_storage):
    name = tests.util.unique_name("test_python_streaming")
    request = oraclebmc.object_storage.models.CreateBucketDetails()
    request.name = name
    request.compartment_id = util.COMPARTMENT_ID
    assert object_storage.create_bucket(namespace, request).status == 200

    yield name

    # Delete new objects and bucket
    try:
        object_list = object_storage.list_objects(namespace, name).data

        for summary in object_list.objects:
            response = object_storage.delete_object(namespace, name, summary.name)
            assert response.status == 200
    except:
        print('TearDown: Could not delete new objects.')

    try:
        object_storage.delete_bucket(namespace, name)
    except:
        print('TearDown: Could not delete new bucket.')


class TestStreaming:
    def test_string_object(self, namespace, bucket_name, object_storage):
        name = 'string_1'
        body = 'This is a test string.'
        response = object_storage.put_object(namespace, bucket_name, name, body)
        assert response.status == 200

        response = object_storage.get_object(namespace, bucket_name, name)
        assert response.status == 200
        assert body == response.data.content.decode('UTF-8')

    def test_text_file_streaming(self, namespace, bucket_name, object_storage):
        name = 'text_file'
        test_file = tests.util.get_resource_path('config')

        # Put an object
        with open(test_file, 'r') as file:
            response = object_storage.put_object(namespace, bucket_name, name, file)
        assert response.status == 200

        # Get it back
        response = object_storage.get_object(namespace, bucket_name, name)
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
        response = object_storage.head_object(namespace, bucket_name, name)
        assert response.status == 200
        assert len(file_content) == int(response.headers['content-length'])

    def test_binary_file_streaming(self, namespace, bucket_name, object_storage):
        name = 'image_file'
        test_file = tests.util.get_resource_path('test_image.png')

        # Put an object
        with open(test_file, 'rb') as file:
            response = object_storage.put_object(namespace, bucket_name, name, file)
        assert response.status == 200

        # Get it back
        response = object_storage.get_object(namespace, bucket_name, name)
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
        response = object_storage.head_object(namespace, bucket_name, name)
        assert response.status == 200
        assert len(file_content) == int(response.headers['content-length'])

    def test_invalid_object_types(self, namespace, bucket_name, object_storage):
        with pytest.raises(TypeError):
            object_storage.put_object(namespace, bucket_name, 'an_int', 24601)

        with pytest.raises(TypeError):
            object_storage.put_object(namespace, bucket_name, 'a_time', time.time())

        with pytest.raises(TypeError):
            object_storage.put_object(namespace, bucket_name, 'a_user', oraclebmc.identity.models.User())

    def test_object_not_found(self, namespace, bucket_name, object_storage):
        with pytest.raises(oraclebmc.exceptions.ServiceError) as excinfo:
            object_storage.get_object(namespace, bucket_name, 'does_not_exist')
        assert excinfo.value.status == 404
