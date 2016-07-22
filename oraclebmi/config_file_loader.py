import ConfigParser
import os.path
import logging
from .config import Config

logger = logging.getLogger(__name__)

class ConfigFileLoader(object):

    DEFAULT_PROFILE = ConfigParser.DEFAULTSECT

    DEFAULT_CONFIG_FILE = '~/.oraclebmi/config'

    @staticmethod
    def load_config(config_file_location=DEFAULT_CONFIG_FILE, profile_name=DEFAULT_PROFILE):
        config_file_location = os.path.expanduser(config_file_location)

        parser = ConfigParser.RawConfigParser()
        if len(parser.read(config_file_location)) != 1:
            raise Exception('Could not load config file at ' + config_file_location)

        config = Config()

        parameters = None
        if profile_name == ConfigFileLoader.DEFAULT_PROFILE:
            parameters = parser.defaults()
        else:
            parameters = parser.options(profile_name)
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
            except:
                logger.info("Error setting Config parameter %s." % param)

        return config

