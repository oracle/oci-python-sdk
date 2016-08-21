from tests.service_test_base import ServiceTestBase
import tests.util
import oraclebmc
import io
import os

class TestLargeFileTransfer(ServiceTestBase):
    """Downloads a large file (2.6 GB) from Object Storage, uploads it to a new bucket, and cleans up."""

    def setUp(self):
        self.context = self.create_context()

        self.read_bucket_name = 'ReadOnlyTestBucket4'
        self.read_object_name = 'reallyLargeFile.dat'

        self.write_object_name = 'file_test'
        self.write_bucket_name = tests.util.unique_name('test_large_file_streaming')

        self.temp_file = tests.util.get_resource_directory() + '/file_download_test_temp_file.dat'
        self.namespace = self.context.object_storage_api.get_namespace().data

        request = oraclebmc.models.CreateBucketDetails()
        request.name = self.write_bucket_name
        request.compartment_id = self.context.config.tenancy
        response = self.context.object_storage_api.create_bucket(self.namespace, request)
        self.assertEqual(200, response.status)

    def tearDown(self):
        # Delete new object, bucket, and file
        try:
            self.context.object_storage_api.delete_object(self.namespace, self.write_bucket_name, self.write_object_name)
        except:
            print('TearDown: Could not delete new object.')

        try:
            self.context.object_storage_api.delete_bucket(self.namespace, self.write_bucket_name)
        except:
            print('TearDown: Could not delete new bucket.')

        try:
            os.remove(self.temp_file)
        except:
            print('TearDown: Could not delete temporary local file.')

    def test_large_file_transfer(self):
        response = self.context.object_storage_api.head_object(self.namespace, self.read_bucket_name, self.read_object_name)
        self.assertEqual(200, response.status)

        content_length = int(response.headers['content-length'])
        print('Downloading file with %s bytes....' % str(content_length))
        next_percent_to_report = 0
        chunk_count = 0;
        total_size = 0;
        chunk_size = 512;
        initial_max_memory_usage = tests.util.max_memory_usage()

        with tests.util.timer('get large file'):
            response = self.context.object_storage_api.get_object(self.namespace, self.read_bucket_name, self.read_object_name)
            self.assertEqual(200, response.status)

            with io.open(self.temp_file, 'wb') as file:
                for chunk in response.data.iter_content(chunk_size=chunk_size):
                    total_size += len(chunk)
                    chunk_count += 1
                    file.write(chunk)
                    percent = total_size * 100 / content_length
                    if percent > next_percent_to_report:
                        print ('%.0f percent complete' % percent)
                        next_percent_to_report += 2

                        # Make sure that memory usage doesn't go too far past where we started.
                        assert (tests.util.max_memory_usage() < 3 * initial_max_memory_usage)

            print('Download complete')

        assert (chunk_count >= (total_size / chunk_size))
        self.assertEqual(total_size, int(response.headers['content-length']))
        file_size = os.path.getsize(self.temp_file)
        self.assertEqual(total_size, file_size)

        print('Uploading to bucket %s with name %s....' % (self.write_bucket_name, self.write_object_name))
        with tests.util.timer('put large file'):
            with open(self.temp_file, 'rb') as file:
                response = self.context.object_storage_api.put_object(self.namespace, self.write_bucket_name, self.write_object_name, file)
                self.assertEqual(200, response.status)

        response = self.context.object_storage_api.head_object(self.namespace, self.write_bucket_name, self.write_object_name)
        self.assertEqual(200, response.status)

        uploaded_content_length = int(response.headers['content-length'])
        self.assertEqual(uploaded_content_length, file_size)

        max_memory = tests.util.max_memory_usage()
        assert(max_memory < file_size)


if __name__ == '__main__':
    unittest.main()