"""
Helpers for loading and validating service configuration.

You can configure services by passing a config dict directly, or by loading
one from a configuration file.

The following keys are required:

    fingerprint
    key_file
    region (or endpoint)
    tenancy
    user

Note that if you provide both "region" and "endpoint" then the endpoint will
be used.

Additionally, the following keys are optional:

    additional_user_agent (default "")
    log_requests (default False)
    pass_phrase (required if your key_file has a passphrase)

At a minimum, you should call config.validate(config_dict) before creating
clients from that config.

"""

from __future__ import absolute_import
import configparser
import os.path
import re
import six

from .exceptions import ConfigFileNotFound, ProfileNotFound, InvalidConfig

__all__ = ["DEFAULT_CONFIG", "from_dict", "from_file", "validate"]

DEFAULT_CONFIG = {
    "log_requests": False,
    "additional_user_agent": "",
    "pass_phrase": None
}
DEFAULT_LOCATION = '~/.oraclebmc/config'
DEFAULT_PROFILE = "DEFAULT"
PATTERNS = {
    # Tenancy and user have the same shape
    "tenancy": re.compile("^([0-9a-zA-Z-_]+[.:])([0-9a-zA-Z-_]*[.:]){3,}([0-9a-zA-Z-_]+)$"),
    "user": re.compile("^([0-9a-zA-Z-_]+[.:])([0-9a-zA-Z-_]*[.:]){3,}([0-9a-zA-Z-_]+)$"),
    "fingerprint": re.compile("^([0-9a-f]{2}:){15}[0-9a-f]{2}$")
}
REQUIRED = {
    "user",
    "tenancy",
    "fingerprint",
    "key_file",
    "region"
}


def from_dict(config):
    """Create a valid config dict from an existing dict.

    This will insert defaults for any missing optional keys, and validate the resulting dict.

        import oraclebmc.config

        # From local variables
        config = oraclebmc.config.load({
            "user": user_ocid,
            "tenancy": tenancy_ocid,
            "fingerprint": fingerprint,
            "region": region
        })

        # From an existing dict, always enable logging
        config = from_somewhere(...)
        config["log_requests"] = True
        config = oraclebmc.config.from_dict(config)
    """
    new_config = dict(config)
    for key, value in six.iteritems(DEFAULT_CONFIG):
        new_config.setdefault(key, value)
    validate(new_config)
    new_config["log_requests"] = _as_bool(new_config["log_requests"])
    new_config["key_file"] = os.path.expanduser(new_config["key_file"])
    return new_config


def from_file(file_location=DEFAULT_LOCATION, profile_name=DEFAULT_PROFILE):
    """Create a valid config dict from a file.

    :param file_location: Path to the config file.  Defaults to ~/.oraclebmc/config
    :param profile_name: The profile to load from the config file.  Defaults to "DEFAULT"
    :return: A config dict that can be used to create clients.
    """
    file_location = os.path.expanduser(file_location)

    parser = configparser.ConfigParser(interpolation=None)
    if not parser.read(file_location):
        raise ConfigFileNotFound("Could not find config file at {!r}".format(file_location))

    if profile_name not in parser:
        raise ProfileNotFound("Profile '{}' not found".format(profile_name))

    # load -> add defaults -> post-process -> validate
    config = dict(parser[profile_name])
    return from_dict(config)


def validate(config):
    """Raises ValueError if required fields are missing or malformed."""
    errors = {}
    for required_key in REQUIRED:
        if required_key not in config:
            errors[required_key] = "missing"

    for key, pattern in six.iteritems(PATTERNS):
        if key in errors:
            # key is missing, can't possibly match pattern
            continue
        if not pattern.match(config[key]):
            errors[key] = "malformed"
    if errors:
        raise InvalidConfig(errors)


def _as_bool(x):
    if x in [True, False]:
        return x
    if x.lower() in ["1", "yes", "true", "on"]:
        return True
    elif x.lower() in ["0", "no", "false", "off"]:
        return False
    else:
        raise ValueError("{!r} is not a valid alias for True/False".format(x))


def _raise_on_errors(errors):
    # report all errors at once
    if len(errors) == 1:
        raise ValueError("Error in config: {}".format(errors[0]))
    elif errors:
        raise ValueError("Found the following config errors: {!r}".format(errors))
