# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import tests.util
from .utils import create_large_file
import io
import hashlib
import base64
import pytest
import os
from oci.object_storage import MultipartObjectAssembler
from oci.fips import is_fips_mode
from oci.object_storage.transfer.internal import md5 as MD5

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


@pytest.mark.skipif(is_fips_mode(),
                    reason="Cannot run test in FIPS mode")
def test_md5(content_input_file):
    """
    This test calculates the md5 for a file using the standard hashlib
    implementation and the internal implementation which is used in
    FIPS mode.
    """

    # calculate md5 using hashlib.  This step won't work in FIPS mode
    # because hashlib.md5 is disabled.
    m = hashlib.md5()
    with io.open(content_input_file, mode='rb') as f:
        while True:
            chunk = f.read(MEBIBYTE)
            m.update(chunk)
            if len(chunk) < MEBIBYTE:
                break

    md5_1 = m.digest()

    # calculate md5 using internal md5 implementation
    m = MD5.md5()
    with io.open(content_input_file, mode='rb') as f:
        while True:
            chunk = f.read(MEBIBYTE)
            m.update(chunk)
            if len(chunk) < MEBIBYTE:
                break

    md5_2 = m.digest()

    assert md5_1 == md5_2


def test_md5_memory_usage(content_input_file):
    starting_memory_usage = tests.util.max_memory_usage()

    # Determine if we can use the hashlib version of md5 or the bundled
    # version of md5
    if is_fips_mode():
        md5 = MD5.md5
    else:
        md5 = hashlib.md5

    m = md5()
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
    # print("Starting memory: {} MiB".format(starting_memory_usage / MEBIBYTE))
    # print("Ending memory: {} MiB".format(ending_memory_usage / MEBIBYTE))
    # print("Memory used: {} MiB".format(str(memory_usage / MEBIBYTE)))
    assert memory_usage < CHUNK
    assert md5_1 == md5_2
