# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import functools
import random
import oci
import os.path
import time
import resource
from contextlib import contextmanager
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from . import test_config_container


def random_number_string():
    if test_config_container.using_vcr_with_mock_responses():
        return '10000'
    else:
        return str(random.randint(0, 10000))


def unique_name(base_name):
    if test_config_container.using_vcr_with_mock_responses():
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
    assert error.headers.get('opc-request-id') is not None
    assert len(error.headers.get('opc-request-id')) == 98

    # Check to string
    for info in [str(status), code, "opc-request-id", message]:
        assert info in str(error)


# Decorates a function with simple/fixed retry behaviour:
#
#    - 3 retries
#    - exponential backoff (2 ^ retry number) between retries
#    - random jitter between 0 to 2 seconds between retries
#
# Retries will also be attempted in the following scenarios:
#
#    - Timeouts
#    - Connection errors
#    - 500s (internal server errors)
#    - Throttles (HTTP 429)
#    - HTTP 409 with a code of "Conflict"
def simple_retries_decorator(func):
    @functools.wraps(func)
    def wrapped_call(*args, **kwargs):
        retry_count = 0
        while (retry_count < 3):
            try:
                return func(*args, **kwargs)
            except (Timeout, ConnectionError) as networking_error:
                retry_count += 1
                post_process_retry(retry_count, 3, networking_error)
            except oci.exceptions.ServiceError as service_error:
                if is_retryable_service_error(service_error):
                    retry_count += 1
                    post_process_retry(retry_count, 3, service_error)
                else:
                    raise

    return wrapped_call


def post_process_retry(retry_count, max_retries, error):
    if retry_count >= max_retries:
        raise error

    time.sleep(2 ** retry_count)  # Backoff
    time.sleep(random.random() * 2)  # Jitter


def is_retryable_service_error(service_error):
    return service_error.status >= 500 or service_error.status == 429 or (service_error.status == 409 and service_error.code == 'Conflict')
