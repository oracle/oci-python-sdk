import configparser
import logging
import os.path
from .config import Config
from . import exceptions

logger = logging.getLogger(__name__)

DEFAULT_PROFILE = configparser.DEFAULTSECT

DEFAULT_CONFIG_FILE = '~/.oraclebmc/config'

def load_config(file_location=DEFAULT_CONFIG_FILE, profile_name=DEFAULT_PROFILE):
    file_location = os.path.expanduser(file_location)

    parser = configparser.RawConfigParser()
    if len(parser.read(file_location)) != 1:
        raise exceptions.ConfigFileNotFound('Could not find config file at ' + file_location)

    config = Config()

    parameters = None
    if profile_name == DEFAULT_PROFILE:
        parameters = parser.defaults()
    else:
        try:
            parameters = parser.options(profile_name)
        except configparser.NoSectionError:
            raise exceptions.ProfileNotFound("Profile '{}' not found".format(profile_name))


    for param in parameters:
        try:
            # getattr will throw if the param does not exist in Config,
            # but setattr will not.
            getattr(config, param)

            value = parser.get(profile_name, param)
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False

            if param == 'key_file':
                value = os.path.expanduser(value)

            setattr(config, param, value)
        except AttributeError:
            logger.info("Error setting Config parameter %s." % param)

    return config

