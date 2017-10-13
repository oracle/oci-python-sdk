import os
import pytest
import oci

from tests.integ import util
from tests.util import get_resource_path
from tests.util import simple_retries_decorator


def pytest_addoption(parser):
    parser.addoption("--config-file", action="store", help="location of the config file",
                     default=get_resource_path('config'))
    parser.addoption("--config-profile", action="store",
                     help="profile to use from the config file",
                     default=oci.config.DEFAULT_PROFILE)


@pytest.fixture
def config_file(request):
    return request.config.getoption("--config-file")


@pytest.fixture
def config_profile(request):
    return request.config.getoption("--config-profile")


@pytest.fixture
def config(config_file, config_profile):
    config = oci.config.from_file(file_location=config_file, profile_name=config_profile)
    util.target_region = config['region']

    pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
    if pass_phrase:
        config['pass_phrase'] = pass_phrase

    util.init_availability_domain_variables(oci.identity.IdentityClient(config), config['tenancy'])

    return config


@pytest.fixture
def object_storage(config):
    return oci.object_storage.ObjectStorageClient(config)


@pytest.fixture
def identity(config_file):
    # Identity throws an error if we do things from not our home region (currently PHX). So use the default profile here, regardless
    # of any command line switches, under the tacit assumption that the default profile points to our home region
    client = oci.identity.IdentityClient(config(config_file, oci.config.DEFAULT_PROFILE))
    add_retries_to_service_operations(client)
    return client


@pytest.fixture
def block_storage(config):
    client = oci.core.BlockstorageClient(config)
    add_retries_to_service_operations(client)
    return client


@pytest.fixture
def compute(config):
    client = oci.core.ComputeClient(config)
    add_retries_to_service_operations(client)
    return client


@pytest.fixture
def virtual_network(config):
    client = oci.core.VirtualNetworkClient(config)
    add_retries_to_service_operations(client)
    return client


@pytest.fixture
def load_balancer_client(config):
    client = oci.load_balancer.LoadBalancerClient(config)
    add_retries_to_service_operations(client)
    return client


@pytest.fixture
def database_client(config):
    client = oci.database.DatabaseClient(config)
    add_retries_to_service_operations(client)
    return client


def add_retries_to_service_operations(client_obj):
    for name in dir(client_obj):
        if name.find('__') == 0:
            continue

        # Replace the method with a decorated version that does retries
        if callable(getattr(client_obj, name)):
            setattr(client_obj, name, simple_retries_decorator(getattr(client_obj, name)))
