# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import random
import oci
import os.path
import time
import resource
from contextlib import contextmanager
from . import test_config_container


def random_number_string():
    if test_config_container.using_vcr_with_mock_responses():
        return '10000'
    else:
        return str(random.randint(0, 10000))


def unique_name(base_name, ignore_vcr=False):
    if test_config_container.using_vcr_with_mock_responses():
        if ignore_vcr:
            return base_name + '_' + str(random.randint(0, 10000))
        else:
            return '{}_vcr'.format(base_name)
    else:
        return base_name + '_' + random_number_string()


def get_resource_directory():
    """Get the absolute path to the test resources directory.
    File is located based on the relative location of this file (util.py).
    """
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "resources")


def get_key_file_path(file_name):
    """Get the absolute path to a file in the keys directory."""
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "..", "keys", file_name)


def get_resource_path(file_name):
    return os.path.join(get_resource_directory(), file_name)


@contextmanager
def timer(name):
    start_time = time.time()
    yield
    total_time = time.time() - start_time
    print('Total time to %s: %.5f seconds' % (name, total_time))


def max_memory_usage():
    """Returns the maximum memory usage of the process so far, in bytes."""
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


def validate_service_error(error, status, code, message):
    assert isinstance(error, oci.exceptions.ServiceError)
    assert error.status == status
    assert error.code == code
    assert error.message.startswith(message)
    assert error.headers is not None
    assert error.request_id.strip()

    if error.headers.get('opc-request-id'):
        assert len(error.headers.get('opc-request-id')) == 98
    else:
        assert len(error.request_id) == 32

    # Check to string
    for info in [str(status), code, "opc-request-id", message]:
        assert info in str(error)
