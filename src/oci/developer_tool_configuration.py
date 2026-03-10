# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import
import re
import os
import logging
import json

import oci.regions
import oci.regions_definitions
from oci.exceptions import InvalidDeveloperToolConfiguration


OCI_DEVELOPER_TOOL_CONFIGURATION_FILE_PATH_ENV_VAR_NAME = "OCI_DEVELOPER_TOOL_CONFIGURATION_FILE_PATH"
DEVELOPER_TOOL_CONFIGURATION_FILE_PATH = os.path.join('~', '.oci', 'developer-tool-configuration.json')

DEVELOPER_TOOL_CONFIGURATION_FILE_SERVICE_KEY_NAME = "services"
DEVELOPER_TOOL_CONFIGURATION_FILE_REGIONS_KEY_NAME = "regions"
DEVELOPER_TOOL_CONFIGURATION_FILE_PROVIDER_KEY_NAME = "developerToolConfigurationProvider"
ALLOW_ONLY_DEVELOPER_TOOL_CONFIGURATION_FILE_KEY_NAME = "allowOnlyDeveloperToolConfigurationRegions"
DEVELOPER_TOOL_CONFIGURATION_FILE_SCHEMA_REQUIRED_KEYS = (
    DEVELOPER_TOOL_CONFIGURATION_FILE_SERVICE_KEY_NAME,
    DEVELOPER_TOOL_CONFIGURATION_FILE_REGIONS_KEY_NAME
)
DEVELOPER_TOOL_CONFIGURATION_FILE_SCHEMA_OPTIONAL_KEYS = (
    ALLOW_ONLY_DEVELOPER_TOOL_CONFIGURATION_FILE_KEY_NAME,
    DEVELOPER_TOOL_CONFIGURATION_FILE_PROVIDER_KEY_NAME
)
logger = logging.getLogger(__name__)


def _enable_developer_tool_configuration_mode():
    if not oci.regions._IS_DEVELOPER_TOOL_CONFIGURATION_MODE:
        logger.debug("Developer tool configuration mode detected")
        oci.regions._IS_DEVELOPER_TOOL_CONFIGURATION_MODE = True


# Class to define the behavior of the set containing services enabled by the developer tool configuration provider
class OciSdkEnabledServicesSet(object):

    def __init__(self):
        self._enabled_services_set = set()
        self._cleared_set_for_user_override = False

    def _clean_up_service_name_string(self, service_name):
        # By default, the OCI Python SDK uses underscores in the module name for services, however, the service names in
        # OCI_SDK_ENABLED_SERVICES_SET are expected without underscores, in lower case
        return re.sub('[^a-z]+', '', service_name.lower())

    def add(self, service_name, override_by_user=True):
        if not self._cleared_set_for_user_override and override_by_user:
            logger.warning("WARNING: Clearing OCI_SDK_ENABLED_SERVICES_SET to allow user override through code")
            self.clear()
            # Set _cleared_set_for_user_override to true, to clear the set only once
            self._cleared_set_for_user_override = True
        clean_service_name_string = self._clean_up_service_name_string(service_name)
        self._enabled_services_set.add(clean_service_name_string)

    def isempty(self):
        return len(self._enabled_services_set) == 0

    def clear(self):
        self._enabled_services_set.clear()

    def is_service_enabled(self, service_name):
        # If OCI_SDK_ENABLED_SERVICES_SET is empty, all the services are enabled
        if self.isempty():
            return True
        clean_service_name_string = self._clean_up_service_name_string(service_name)
        return clean_service_name_string in self._enabled_services_set


OCI_SDK_ENABLED_SERVICES_SET = OciSdkEnabledServicesSet()


def _validate_developer_tool_configuration_file_schema(config_json_object):
    for key in DEVELOPER_TOOL_CONFIGURATION_FILE_SCHEMA_REQUIRED_KEYS:
        if key not in config_json_object:
            logger.debug("Key {} not found in developer tool configuration file".format(key))
            raise InvalidDeveloperToolConfiguration("Developer Tool Configuration is invalid. Missing required key {}".format(key))
    for key in DEVELOPER_TOOL_CONFIGURATION_FILE_SCHEMA_OPTIONAL_KEYS:
        if key in config_json_object and key is ALLOW_ONLY_DEVELOPER_TOOL_CONFIGURATION_FILE_KEY_NAME:
            if not isinstance(config_json_object[key], (bool, str)):
                raise InvalidDeveloperToolConfiguration("{} must be either bool or str".format(ALLOW_ONLY_DEVELOPER_TOOL_CONFIGURATION_FILE_KEY_NAME))
            if isinstance(config_json_object[key], str) and config_json_object[key].lower() not in ("true", "false"):
                raise InvalidDeveloperToolConfiguration("Allowed values for {} are either true or false".format(ALLOW_ONLY_DEVELOPER_TOOL_CONFIGURATION_FILE_KEY_NAME))
    return True


def _add_services_from_developer_tool_configuration_file(config_services_list):
    if config_services_list:
        for service in config_services_list:
            OCI_SDK_ENABLED_SERVICES_SET.add(service, override_by_user=False)


def _set_config_from_developer_tool_configuration_file():
    """
    Looks for developer-tool-configuration.json and parses enabled services and regions information from it
    Default location is ~/.oci/developer-tool-configuration.json
    Default location can be overridden by setting environment variable OCI_DEVELOPER_TOOL_CONFIGURATION_FILE_PATH
    """
    if os.getenv(OCI_DEVELOPER_TOOL_CONFIGURATION_FILE_PATH_ENV_VAR_NAME):
        config_file_location = os.getenv(OCI_DEVELOPER_TOOL_CONFIGURATION_FILE_PATH_ENV_VAR_NAME)
        logger.debug("Overriding default path for developer-tool-configuration.json to {}".format(OCI_DEVELOPER_TOOL_CONFIGURATION_FILE_PATH_ENV_VAR_NAME))
    else:
        config_file_location = DEVELOPER_TOOL_CONFIGURATION_FILE_PATH
    expanded_file_location = os.path.expanduser(config_file_location)
    if os.path.isfile(expanded_file_location):
        _enable_developer_tool_configuration_mode()
        logger.debug("Developer tool configuration file found at location {}".format(expanded_file_location))
        try:
            with open(expanded_file_location, 'r') as developer_tool_configuration_file:
                developer_tool_configuration_raw_file_content = developer_tool_configuration_file.read()
        except (OSError, IOError) as e:
            logger.debug("Reading developer tool configuration file failed because of error: {}".format(e))
            raise e
        try:
            developer_tool_configuration_json_object = json.loads(developer_tool_configuration_raw_file_content)
        except json.JSONDecodeError as e:
            # Unable to parse the json array
            logger.debug("Decoding JSON array from developer tool configuration file failed because of error: {}".format(e))
            raise e

        if _validate_developer_tool_configuration_file_schema(developer_tool_configuration_json_object):
            # Extract enabled services and regions from developer_tool_configuration_json_object
            _add_services_from_developer_tool_configuration_file(developer_tool_configuration_json_object[DEVELOPER_TOOL_CONFIGURATION_FILE_SERVICE_KEY_NAME])
            oci.regions._ALLOW_ONLY_DEVELOPER_TOOL_CONFIGURATION_REGIONS = developer_tool_configuration_json_object.get(ALLOW_ONLY_DEVELOPER_TOOL_CONFIGURATION_FILE_KEY_NAME, False)
            oci.regions._process_region_metadata_from_developer_tool_configuration_file(developer_tool_configuration_json_object[DEVELOPER_TOOL_CONFIGURATION_FILE_REGIONS_KEY_NAME])
            oci.regions.DEVELOPER_TOOL_CONFIGURATION_PROVIDER_NAME = developer_tool_configuration_json_object.get(DEVELOPER_TOOL_CONFIGURATION_FILE_PROVIDER_KEY_NAME, False)


def _config_developer_tool_configuration_mode():
    """
    Determines if developer tool configuration inputs are provided and configures the SDK for developer tool configuration mode
    Developer tool configuration mode is enabled if developer-tool-configuration.json file is found
    """
    # Read all the sources to determine developer tool configuration mode
    _set_config_from_developer_tool_configuration_file()


_config_developer_tool_configuration_mode()
