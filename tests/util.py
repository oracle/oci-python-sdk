import random
import os.path
import time
import resource
from contextlib import contextmanager


def random_number_string():
    return str(random.randint(0, 10000))


def unique_name(base_name):
    return base_name + '_' + random_number_string()


def get_resource_directory():
    """Get the relative path to the test resources directory.
    This will change depending on where the tests are run."""
    path = 'resources'
    if os.path.isdir(path):
        return path

    path = 'tests/' + path
    if os.path.isdir(path):
        return path


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
