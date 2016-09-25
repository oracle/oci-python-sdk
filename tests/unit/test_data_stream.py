from tests.service_test_base import ServiceTestBase
import oraclebmc


class TestDataStream(ServiceTestBase):
    """Tests the oraclebmc.DataStream object."""

    def setUp(self):
        self.config = self.create_config()

        self.namespace = 'internalbriangustafson'
        self.bucket_name = 'ReadOnlyTestBucket2'
        self.object_name = 'a/b/c/object3'
        self.expected_content = self.object_name

        # Get the object
        object_storage = oraclebmc.apis.ObjectStorageApi(self.config)
        self.response = object_storage.get_object(
            self.namespace,
            self.bucket_name,
            self.object_name
        )
        assert self.response.status == 200

    def test_content(self):
        assert self.expected_content == self.response.data.content.decode('UTF-8')

    def test_iter_content(self):
        response_text = ''
        chunk_count = 0
        chunk_size = 2
        for chunk in self.response.data.iter_content(chunk_size=chunk_size):
            response_text += chunk.decode('UTF-8')
            chunk_count += 1

        assert chunk_count >= (len(self.expected_content) / chunk_size)
        assert response_text == self.expected_content

    def test_raw(self):
        response_text = self.response.data.raw.read(100).decode('UTF-8')
        assert response_text == self.expected_content

    def test_content_multiple_access(self):
        assert self.expected_content == self.response.data.content.decode('UTF-8')
        assert self.expected_content == self.response.data.content.decode('UTF-8')
        assert self.expected_content == self.response.data.content.decode('UTF-8')

    def test_stream_after_content(self):
        assert self.expected_content == self.response.data.content.decode('UTF-8')

        response_text = ''
        chunk_count = 0
        chunk_size = 2
        for chunk in self.response.data.iter_content(chunk_size=chunk_size):
            response_text += chunk.decode('UTF-8')
            chunk_count += 1

        assert chunk_count >= (len(self.expected_content) / chunk_size)
        assert response_text == self.expected_content

    def test_content_after_stream(self):
        response_text = ''
        for chunk in self.response.data.iter_content():
            response_text += chunk.decode('UTF-8')
        assert response_text == self.expected_content

        with self.assertRaises(oraclebmc.exceptions.StreamAlreadyConsumed):
            # content was already consumed by iter_content above
            getattr(self.response.data, "content")

    def test_stream_twice(self):
        response_text = ''
        for chunk in self.response.data.iter_content():
            response_text += chunk.decode('UTF-8')
        assert response_text == self.expected_content

        with self.assertRaises(oraclebmc.exceptions.StreamAlreadyConsumed):
            for chunk in self.response.data.iter_content():
                response_text += chunk.decode('UTF-8')
