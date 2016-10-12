import tests.util
import oraclebmc
import io
import os
import pytest


@pytest.fixture
def namespace(object_storage):
    return object_storage.get_namespace().data


@pytest.fixture
def names():
    return {
        "read-object": "reallyLargeFile.dat",
        "read-bucket": "ReadOnlyTestBucket4",
        "write-object": "file_test",
        "write-bucket": tests.util.unique_name("test_python_streaming"),
        "temp-file": tests.util.get_resource_directory() + "/file_download_test_temp_file.dat"
    }


@pytest.yield_fixture
def write_bucket(namespace, object_storage, config, names):
    request = oraclebmc.models.CreateBucketDetails()
    request.name = names["write-bucket"]
    request.compartment_id = config["tenancy"]
    response = object_storage.create_bucket(namespace, request)
    assert response.status == 200

    bucket = response.data

    yield bucket

    # Delete new objects and bucket
    try:
        object_list = object_storage.list_objects(namespace, bucket.name).data

        for summary in object_list.objects:
            response = object_storage.delete_object(namespace, bucket.name, summary.name)
            assert response.status == 200
    except:
        print('TearDown: Could not delete new object.')

    try:
        object_storage.delete_bucket(namespace, bucket.name)
    except:
        print('TearDown: Could not delete new bucket.')

    try:
        os.remove(names["temp-file"])
    except:
        print('TearDown: Could not delete temporary local file.')


def test_large_file_transfer(namespace, object_storage, names):
    """Download, upload, and delete a large file (2.6 GB)"""
    response = object_storage.head_object(
        namespace,
        names["read-bucket"],
        names["read-object"]
    )
    assert response.status == 200

    content_length = int(response.headers['content-length'])
    print('Downloading file with %s bytes....' % str(content_length))
    next_percent_to_report = 0
    chunk_count = 0
    total_size = 0
    chunk_size = 512
    initial_max_memory_usage = tests.util.max_memory_usage()

    with tests.util.timer('get large file'):
        response = object_storage.get_object(
            namespace,
            names["read-bucket"],
            names["read-object"]
        )
        assert response.status == 200
        with io.open(names["temp-file"], 'wb') as file:
            for chunk in response.data.iter_content(chunk_size=chunk_size):
                total_size += len(chunk)
                chunk_count += 1
                file.write(chunk)
                percent = total_size * 100 / content_length
                if percent > next_percent_to_report:
                    print('%.0f percent complete' % percent)
                    next_percent_to_report += 2

                    # Make sure that memory usage doesn't go too far past where we started.
                    assert tests.util.max_memory_usage() < 3 * initial_max_memory_usage

        print('Download complete')

    assert chunk_count >= (total_size / chunk_size)
    assert total_size == int(response.headers['content-length'])
    file_size = os.path.getsize(names["temp-file"])
    assert total_size == file_size

    upload_msg = 'Uploading to bucket {} with name {}....'
    print(upload_msg.format(names["write-bucket"], names["write-object"]))
    with tests.util.timer('put large file'):
        with io.open(names["temp-file"], 'rb') as file:
            response = object_storage.put_object(
                namespace,
                names["write-bucket"],
                names["write-object"],
                file
            )
            assert response.status == 200

    response = object_storage.head_object(
        namespace,
        names["write-bucket"],
        names["write-object"]
    )
    assert response.status == 200

    uploaded_content_length = int(response.headers['content-length'])
    assert uploaded_content_length == file_size

    max_memory = tests.util.max_memory_usage()
    assert max_memory < file_size
