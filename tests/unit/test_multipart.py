import tests.util
from .utils import create_large_file
import io
import hashlib
import base64
import pytest
import os
from oci.object_storage import MultipartObjectAssembler

MEBIBYTE = 1024 * 1024
CHUNK = 128 * MEBIBYTE
LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES = 150


@pytest.fixture(scope='function')
def content_input_file():
    filename = 'tests/resources/multipart_content_input.txt'

    # generate large file for multipart testing
    create_large_file(filename, LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)

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
