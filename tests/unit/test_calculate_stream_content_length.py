# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

try:
    import unittest.mock as mock
except ImportError:
    import mock

import oci
import os
import oci.retry
import pytest
import tests.util


class FileLikeBody:
    def __init__(self,
                 no_read=None,
                 no_seek=None,
                 bad_seek=None,
                 no_tell=None,
                 bad_tell=None):
        if not no_read:
            self.read = mock.Mock()

        if not no_seek:
            if bad_seek:
                mock_seek = mock.Mock()
                mock_seek.side_effect = IOError
                self.seek = mock_seek
            else:
                mock_seek = mock.Mock()
                self.seek = mock_seek

        if not no_tell:
            if bad_tell:
                mock_tell = mock.Mock()
                mock_tell.side_effect = OSError
                self.tell = mock_tell
            else:
                mock_tell = mock.Mock()
                mock_tell.return_value = 5
                self.tell = mock_tell


def test_failed_calculation_for_string_body():
    with pytest.raises(TypeError):
        oci.util.back_up_body_calculate_stream_content_length("StringBody")


def test_failed_with_no_read_property():
    stream_obj = FileLikeBody(no_read=True)
    with pytest.raises(TypeError):
        oci.util.back_up_body_calculate_stream_content_length(stream_obj)


def test_failed_with_small_buffer_limit():
    test_file = tests.util.get_resource_path('test_image.png')
    with pytest.raises(BufferError):
        with open(test_file, 'rb') as file:
            oci.util.back_up_body_calculate_stream_content_length(file, 1)


def test_stream_content_length():
    test_file = tests.util.get_resource_path('test_image.png')
    with open(test_file, 'rb') as file:
        calculated_content_length = oci.util.back_up_body_calculate_stream_content_length(file, None)
        verify_content_length = os.fstat(file.fileno()).st_size
    assert calculated_content_length['content_length'] == verify_content_length
