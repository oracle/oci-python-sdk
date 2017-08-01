import os
import pytest
import oraclebmc

from tests.integ import util
from tests.util import get_resource_path

def pytest_addoption(parser):
    parser.addoption("--config-file", action="store", help="location of the config file",
                     default=get_resource_path('config'))
    parser.addoption("--config-profile", action="store",
                     help="profile to use from the config file",
                     default=oraclebmc.config.DEFAULT_PROFILE)


@pytest.fixture
def config_file(request):
    return request.config.getoption("--config-file")

@pytest.fixture
def config_profile(request):
    return request.config.getoption("--config-profile")


@pytest.fixture
def config(config_file, config_profile):
    config = oraclebmc.config.from_file(file_location=config_file, profile_name=config_profile)
    util.target_region = config['region']
    pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
    if pass_phrase:
        config['pass_phrase'] = pass_phrase
    return config

@pytest.fixture
def object_storage(config):
    return oraclebmc.object_storage.ObjectStorageClient(config)


@pytest.fixture
def identity(config_file):
    # Identity throws an error if we do things from not our home region (currently PHX). So use the default profile here, regardless
    # of any command line switches, under the tacit assumption that the default profile points to our home region
    return oraclebmc.identity.IdentityClient(config(config_file, oraclebmc.config.DEFAULT_PROFILE))


@pytest.fixture
def block_storage(config):
    return oraclebmc.core.BlockstorageClient(config)


@pytest.fixture
def compute(config):
    return oraclebmc.core.ComputeClient(config)


@pytest.fixture
def virtual_network(config):
    return oraclebmc.core.VirtualNetworkClient(config)


@pytest.fixture
def load_balancer_client(config):
    return oraclebmc.load_balancer.LoadBalancerClient(config)
