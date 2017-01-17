import random
import oraclebmc
import os.path
import time
import resource
from contextlib import contextmanager


def random_number_string():
    return str(random.randint(0, 10000))


def unique_name(base_name):
    return base_name + '_' + random_number_string()


def get_resource_directory():
    """Get the absolute path to the test resources directory.
    File is located based on the relative location of this file (util.py).
    """
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "resources")


def get_resource_path(file_name):
    return get_resource_directory() + '/' + file_name


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
    assert isinstance(error, oraclebmc.exceptions.ServiceError)
    assert error.status == status
    assert error.code == code
    assert error.message.startswith(message)
    assert error.headers is not None
    assert error.headers.get('opc-request-id') is not None
    assert len(error.headers.get('opc-request-id')) == 98

    # Check to string
    for info in [str(status), code, "opc-request-id", message]:
        assert info in str(error)
