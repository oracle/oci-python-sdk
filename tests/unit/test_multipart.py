import tests.util
import utils
import io
import hashlib
import base64
import oraclebmc
import pytest
import os
from oraclebmc.object_storage import MultipartObjectAssembler

MEBIBYTE = 1024 * 1024
CHUNK = 128 * MEBIBYTE

LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES = 150


@pytest.fixture(scope='function')
def content_input_file():
    filename = 'tests/resources/multipart_content_input.txt'

    # generate large file for multipart testing
    utils.create_large_file(filename, LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)

    yield filename

    if os.path.exists(filename):
        os.remove(filename)


def test_md5_memory_usage(content_input_file):
    starting_memory_usage = tests.util.max_memory_usage()

    m = hashlib.md5()
    with io.open(content_input_file, mode='rb') as f:
        file_size = os.fstat(f.fileno()).st_size
        while True:
            chunk = f.read(MEBIBYTE)
            m.update(chunk)
            if len(chunk) < MEBIBYTE:
                break

    md5_1 = base64.b64encode(m.digest()).decode("utf-8")

    md5_2 = MultipartObjectAssembler.calculate_md5(content_input_file,
                                                   0,
                                                   file_size)

    ending_memory_usage = tests.util.max_memory_usage()
    memory_usage = ending_memory_usage - starting_memory_usage
    print("Starting memory: {} MiB".format(starting_memory_usage / MEBIBYTE))
    print("Ending memory: {} MiB".format(ending_memory_usage / MEBIBYTE))
    print("Memory used: {} MiB".format(str(memory_usage / MEBIBYTE)))
    assert memory_usage < CHUNK
    assert md5_1 == md5_2


@pytest.mark.skip("Clean this up and move to integ.")
def test_multipart_upload_memory_usage():
    up = oraclebmc.object_storage.UploadManager
    config = oraclebmc.config.from_file()
    object_storage = oraclebmc.object_storage.ObjectStorageClient(config)
    namespace_name = object_storage.get_namespace().data
    bucket_name = "DEX-836_multipart_uploads"

    up.upload(object_storage,
              namespace_name,
              bucket_name,
              'memory_usage_test',
              open('/Users/ahalliii/Downloads/pycharm-professional-2017.1.dmg', 'rb'),
              part_size=CHUNK)

    max_memory = tests.util.max_memory_usage()
    print("Max memory usage with bufferedpartreader: {} MiB".format(str(max_memory / MEBIBYTE)))
    assert max_memory < CHUNK
