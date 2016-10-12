import os.path
import oraclebmc

import pytest

from tests.util import get_resource_path

DEFAULT_REGION = "us-phoenix-1"
HARDCODED_TENANCY = "ocidv1:tenancy:region:az:1457568341552:aaaaaaaak5kqrgabmglda4oz7mcdedhuym"
HARDCODED_USER = "ocid1.user.region..1461711049110:aaaaaaaaeuhzapiritehle2dmrcoeijvve"
HARDCODED_FINGERPRINT = "20:3b:97:13:55:1c:5b:0d:d3:37:d8:50:4e:c5:3a:34"
HARDCODED_KEYFILE = "~/.ssh/id_rsa.pem"
HARDCODED_REGION = "us-phoenix-1"


def test_load_default_profile():
    config = oraclebmc.config.from_file(file_location=get_resource_path('config'))

    # check some default properties
    assert config["log_requests"] is False

    # check properties set in file
    assert config["tenancy"] == HARDCODED_TENANCY
    assert config["user"] == HARDCODED_USER
    assert config["fingerprint"] == HARDCODED_FINGERPRINT
    assert config["endpoints"] == oraclebmc.regions.get_endpoints(HARDCODED_REGION)
    assert config["key_file"] == os.path.expanduser(HARDCODED_KEYFILE)


def test_child_profile():
    config = oraclebmc.config.from_file(
        file_location=get_resource_path('config'), profile_name='DEBUG')

    # check some default properties
    assert config["verify_ssl"]

    # check properties inherited from the default profile
    assert config["tenancy"] == HARDCODED_TENANCY
    assert config["user"] == HARDCODED_USER
    assert config["fingerprint"] == HARDCODED_FINGERPRINT

    # check properties overridden by the specified profile
    assert config["log_requests"]
    assert config["additional_user_agent"]


def test_extra_config_values():
    # Extra config is passed along; this may be customer-specific
    # config for some subclass of the clients.
    config = oraclebmc.config.from_file(
        file_location=get_resource_path('config'), profile_name='INVALID_PARAMETER')
    assert config["foo"] == "bar"


def test_file_not_found():
    with pytest.raises(oraclebmc.exceptions.ConfigFileNotFound) as excinfo:
        oraclebmc.config.from_file(file_location='does_not_exist')
    assert 'does_not_exist' in str(excinfo.value)


def test_profile_not_found():
    with pytest.raises(oraclebmc.exceptions.ProfileNotFound) as excinfo:
        oraclebmc.config.from_file(profile_name='does_not_exist')
    assert 'does_not_exist' in str(excinfo.value)


def test_invalid_region():
    with pytest.raises(ValueError) as excinfo:
        oraclebmc.config.from_file(
            get_resource_path('config'),
            profile_name='INVALID_REGION')
    assert "'whoami' is not a recognized region" in str(excinfo.value)
