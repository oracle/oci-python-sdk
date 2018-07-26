# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

"""
Helpers for loading and validating service configuration.

You can configure services by passing a config dict directly, or by loading
one from a configuration file.

The following keys are required::

    fingerprint
    key_file
    region
    tenancy
    user

Additionally, the following keys are optional::

    additional_user_agent (default "")
    log_requests (default False)
    pass_phrase (required if your key_file has a passphrase)

"""

from __future__ import absolute_import
import configparser
import os.path
import re
from oci._vendor import six

from .exceptions import ConfigFileNotFound, ProfileNotFound, InvalidConfig
from .auth import signers

__all__ = ["DEFAULT_CONFIG", "from_file", "validate_config"]

DEFAULT_CONFIG = {
    "log_requests": False,
    "additional_user_agent": "",
    "pass_phrase": None
}
DEFAULT_LOCATION = os.path.join('~', '.oci', 'config')
FALLBACK_DEFAULT_LOCATION = os.path.join('~', '.oraclebmc', 'config')
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
REQUIRED_FALLBACKS = {
    "key_file": "key_content"
}
CONFIG_FILE_BLACKLISTED_KEYS = {
    "key_content"
}


def from_file(file_location=DEFAULT_LOCATION, profile_name=DEFAULT_PROFILE):
    """Create a config dict from a file.

    :param file_location: Path to the config file.  Defaults to ~/.oci/config and with a fallback to ~/.oraclebmc/config.
    :param profile_name: The profile to load from the config file.  Defaults to "DEFAULT"
    :return: A config dict that can be used to create clients.
    """
    expanded_file_location = _get_config_path_with_fallback(file_location)

    parser = configparser.ConfigParser(interpolation=None)
    if not parser.read(expanded_file_location):
        raise ConfigFileNotFound("Could not find config file at {}".format(expanded_file_location))

    if profile_name not in parser:
        raise ProfileNotFound("Profile '{}' not found in config file {}".format(profile_name, expanded_file_location))

    config = dict(DEFAULT_CONFIG)
    config.update(parser[profile_name])
    config["log_requests"] = _as_bool(config["log_requests"])

    for key in CONFIG_FILE_BLACKLISTED_KEYS:
        if key in config:
            raise ValueError("'{}' cannot be specified in a config file for security reasons. To use this key you must add it to the config programmatically.".format(key))

    return config


def validate_config(config, **kwargs):
    if 'signer' in kwargs:
        # The InstancePrincipalsSecurityTokenSigner is self-sufficient and doesn't need to read
        # the normally-required keys in the config
        if isinstance(kwargs['signer'], signers.InstancePrincipalsSecurityTokenSigner):
            return

    """Raises ValueError if required fields are missing or malformed."""
    errors = {}
    for required_key in REQUIRED:
        fallback_key = REQUIRED_FALLBACKS.get(required_key)
        if required_key not in config and fallback_key not in config:
            errors[required_key] = "missing"

    for key, pattern in six.iteritems(PATTERNS):
        if key in errors:
            # key is missing, can't possibly match pattern
            continue
        if not pattern.match(config[key]):
            errors[key] = "malformed"
    if errors:
        raise InvalidConfig(errors)


def get_config_value_or_default(config, key):
    return config.get(key, DEFAULT_CONFIG.get(key))


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


def _get_config_path_with_fallback(file_location):
    expanded_file_location = os.path.expanduser(file_location)
    expanded_fallback_default_file_location = os.path.expanduser(FALLBACK_DEFAULT_LOCATION)

    # if there is no file in the default location (~/.oci/config), and the fallback file does exist, use the fallback (~/.oraclebmc/config)
    if file_location == DEFAULT_LOCATION and not os.path.isfile(expanded_file_location) and os.path.isfile(expanded_fallback_default_file_location):
        expanded_file_location = expanded_fallback_default_file_location

    return expanded_file_location
