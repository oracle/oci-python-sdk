import pytest

import oraclebmc
import tests.util


@pytest.fixture
def config():
    return oraclebmc.config_file_loader.load_config(
        file_location=tests.util.get_resource_path('config'),
        profile_name=oraclebmc.config_file_loader.DEFAULT_PROFILE
    )


@pytest.fixture
def object_storage(config):
    return oraclebmc.apis.ObjectStorageApi(config)


@pytest.fixture
def virtual_network(config):
    return oraclebmc.apis.VirtualNetworkApi(config)


@pytest.fixture
def identity(config):
    return oraclebmc.apis.IdentityApi(config)


@pytest.fixture
def compute(config):
    return oraclebmc.apis.ComputeApi(config)


@pytest.fixture
def block_storage(config):
    return oraclebmc.apis.BlockstorageApi(config)
