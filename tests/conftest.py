import pytest
import oraclebmc


def pytest_addoption(parser):
    parser.addoption("--config-file", action="store", help="location of the config file",
                     default=oraclebmc.config_file_loader.DEFAULT_CONFIG_FILE)
    parser.addoption("--config-profile", action="store",
                     help="profile to use from the config file",
                     default=oraclebmc.config_file_loader.DEFAULT_PROFILE)


@pytest.fixture
def config(request):
    return oraclebmc.config_file_loader.load_config(
        file_location=request.config.getoption("--config-file"),
        profile_name=request.config.getoption("--config-profile")
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
