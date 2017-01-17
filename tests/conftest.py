import pytest
import oraclebmc


def pytest_addoption(parser):
    parser.addoption("--config-file", action="store", help="location of the config file",
                     default=oraclebmc.config.DEFAULT_LOCATION)
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
    return oraclebmc.config.from_file(
        file_location=config_file,
        profile_name=config_profile
    )


@pytest.fixture
def object_storage(config):
    return oraclebmc.object_storage.ObjectStorageClient(config)


@pytest.fixture
def identity(config):
    return oraclebmc.identity.IdentityClient(config)
