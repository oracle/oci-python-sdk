# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import
import os
import json
import logging
from enum import Enum

from . import service_endpoints
from oci._vendor import six
from oci._vendor import requests
from oci._vendor.requests.exceptions import HTTPError, ConnectionError, RetryError
from oci._vendor.requests.adapters import HTTPAdapter
from oci._vendor.urllib3.util.retry import Retry

REGIONS_SHORT_NAMES = {
    'phx': 'us-phoenix-1',
    'iad': 'us-ashburn-1',
    'sjc': 'us-sanjose-1',
    'fra': 'eu-frankfurt-1',
    'zrh': 'eu-zurich-1',
    'cwl': 'uk-cardiff-1',
    'lhr': 'uk-london-1',
    'yyz': 'ca-toronto-1',
    'nrt': 'ap-tokyo-1',
    'icn': 'ap-seoul-1',
    'bom': 'ap-mumbai-1',
    'gru': 'sa-saopaulo-1',
    'syd': 'ap-sydney-1',
    'ltn': 'uk-gov-london-1',
    'kix': 'ap-osaka-1',
    'mel': 'ap-melbourne-1',
    'ams': 'eu-amsterdam-1',
    'jed': 'me-jeddah-1',
    'yul': 'ca-montreal-1',
    'hyd': 'ap-hyderabad-1',
    'yny': 'ap-chuncheon-1',
    'brs': 'uk-gov-cardiff-1',
    'nja': 'ap-chiyoda-1',
    'dxb': 'me-dubai-1'
}
REGION_REALMS = {
    'ap-melbourne-1': 'oc1',
    'ap-mumbai-1': 'oc1',
    'ap-hyderabad-1': 'oc1',
    'ap-osaka-1': 'oc1',
    'ap-seoul-1': 'oc1',
    'ap-sydney-1': 'oc1',
    'ap-tokyo-1': 'oc1',
    'ap-chuncheon-1': 'oc1',
    'us-phoenix-1': 'oc1',
    'us-ashburn-1': 'oc1',
    'us-sanjose-1': 'oc1',
    'eu-amsterdam-1': 'oc1',
    'eu-frankfurt-1': 'oc1',
    'eu-zurich-1': 'oc1',
    'me-dubai-1': 'oc1',
    'me-jeddah-1': 'oc1',
    'uk-cardiff-1': 'oc1',
    'uk-london-1': 'oc1',
    'ca-toronto-1': 'oc1',
    'sa-saopaulo-1': 'oc1',
    'ca-montreal-1': 'oc1',

    'us-langley-1': 'oc2',
    'us-luke-1': 'oc2',

    'us-gov-ashburn-1': 'oc3',
    'us-gov-chicago-1': 'oc3',
    'us-gov-phoenix-1': 'oc3',

    'uk-gov-london-1': 'oc4',
    'uk-gov-cardiff-1': 'oc4',

    'ap-chiyoda-1': 'oc8'
}
REALMS = {
    'oc1': 'oraclecloud.com',
    'oc2': 'oraclegovcloud.com',
    'oc3': 'oraclegovcloud.com',
    'oc4': 'oraclegovcloud.uk',
    'oc8': 'oraclecloud8.com'
}
REGIONS = [
    "ap-melbourne-1",
    "ap-mumbai-1",
    "ap-hyderabad-1",
    "ap-osaka-1",
    "ap-seoul-1",
    "ap-sydney-1",
    "ap-tokyo-1",
    "ap-chuncheon-1",
    "ap-chiyoda-1",
    "us-phoenix-1",
    "us-ashburn-1",
    "us-sanjose-1",
    "eu-amsterdam-1",
    "eu-frankfurt-1",
    "eu-zurich-1",
    "me-dubai-1",
    "me-jeddah-1",
    "uk-cardiff-1",
    "uk-london-1",
    "uk-gov-cardiff-1",
    "ca-toronto-1",
    "ca-montreal-1",
    "us-langley-1",
    "us-luke-1",
    "us-gov-ashburn-1",
    "us-gov-chicago-1",
    "us-gov-phoenix-1",
    "sa-saopaulo-1",
    "uk-gov-london-1"
]
SERVICE_ENDPOINTS = service_endpoints.SERVICE_ENDPOINTS
SERVICE_ENDPOINTS['auth'] = 'https://auth.{domain}'

DOMAIN_FORMAT = "{region}.{secondLevelDomain}"

OCI_REGION_METADATA_ENV_VAR_NAME = "OCI_REGION_METADATA"

REALM_KEY_PROPERTY_NAME = "realmKey"
REALM_DOMAIN_COMPONENT_PROPERTY_NAME = "realmDomainComponent"
REGION_KEY_PROPERTY_NAME = "regionKey"
REGION_IDENTIFIER_PROPERTY_NAME = "regionIdentifier"

# Region Metadata schema
REGION_METADATA_KEYS = (REALM_KEY_PROPERTY_NAME,
                        REALM_DOMAIN_COMPONENT_PROPERTY_NAME,
                        REGION_KEY_PROPERTY_NAME,
                        REGION_IDENTIFIER_PROPERTY_NAME)

# Constants for getting region info from IMDS
METADATA_URL_BASE = 'http://169.254.169.254/opc/v2'
GET_REGION_URL = '{}/instance/regionInfo'.format(METADATA_URL_BASE)
METADATA_AUTH_HEADERS = {'Authorization': 'Bearer Oracle'}

# Constants for regions config file
REGIONS_CONFIG_FILE_PATH = os.path.join('~', '.oci', 'regions-config.json')

# Enumerate region information sources outside of lookups
ExternalSources = Enum('ExternalSources', ['REGIONS_CFG_FILE', 'ENV_VAR', 'IMDS'])

# Dict to track if we have read the ExternalSources
# Reading from IMDS is opt-in and can be enabled by calling enable_instance_metadata_service()
_has_been_read_external_sources = {
    ExternalSources.REGIONS_CFG_FILE: False,
    ExternalSources.ENV_VAR: False,
    ExternalSources.IMDS: True
}

logger = logging.getLogger(__name__)


def is_region(region_name):
    region = region_name.lower()

    if region in REGIONS_SHORT_NAMES:
        return False
    if region not in REGIONS:
        return _check_and_add_region_metadata(region)
    return True


def is_region_short_name(region):
    region = region.lower()
    if region in REGIONS_SHORT_NAMES:
        return True

    if region in REGIONS:
        return False

    if _check_and_add_region_metadata(region):
        # Above call will return true if the requested region is now known, after considering additional sources
        # Check is needed if region short code was passed
        if region in REGIONS_SHORT_NAMES:
            return True

    return False


def get_region_from_short_name(region):
    region = region.lower()
    if not is_region_short_name(region):
        logger.debug("Could not find region information in lookups and any other sources")
        # Return the input string to allow fallback to OC1
        return region
    # Return region from lookup
    return REGIONS_SHORT_NAMES[region]


def get_realm_from_region(region):
    region = region.lower()
    # If short name is passed, get the long name
    # get_region_from_short_name also adds metadata from other sources
    region = get_region_from_short_name(region)
    if not is_region(region):
        logger.debug("Cannot find region information in lookups and other sources, defaulting to OC1 realm")
        return "oc1"
    else:
        return REGION_REALMS[region]


def endpoint_for(service, region=None, endpoint=None, service_endpoint_template=None):
    """Returns the base URl for a service, either in the given region or at the specified endpoint.

    If endpoint and region are provided, endpoint is used.

    If the region information is not available in the existing maps, following sources are checked in order:
    1. Regions Configuration File at ~/.oci/regions-config.json
    2. Region Metadata Environment variable
    3. Instance Metadata Service

    Lookup from Instance Metadata Service is disabled by default. To enable, call enable_instance_metadata_service()

    The region metadata schema is:
    {
        "realmKey" : string,
        "realmDomainComponent" : string,
        "regionKey" : string,
        "regionIdentifier" : string
    }

    For example,  for the Sydney OC1 region, the schema would be filled out as follows:
    {
        "realmKey" : "OC1",
        "realmDomainComponent" : "oraclecloud.com",
        "regionKey" : "SYD",
        "regionIdentifier" : "ap-sydney-1"
     }

    If the region still cannot be resolved, we fall back to OC1 realm
    """
    if not (endpoint or region):
        raise ValueError("Must supply either a region or an endpoint.")

    if endpoint:
        # endpoint takes priority
        return _format_endpoint(service, endpoint, service_endpoint_template)

    region = region.lower()
    # If unable to find region information from existing maps, check the other sources and add
    if not (region in REGIONS or region in REGIONS_SHORT_NAMES):
        _check_and_add_region_metadata(region)
    return _endpoint_for(service, region, service_endpoint_template)


def skip_instance_metadata_service():
    logger.debug("Disabling region metadata lookup from IMDS")
    _set_source_has_been_read(ExternalSources.IMDS)


def enable_instance_metadata_service():
    logger.debug("Enabling region metadata lookup from IMDS")
    _set_source_has_been_read(ExternalSources.IMDS, False)


def _set_source_has_been_read(source, value=True):
    _has_been_read_external_sources[source] = value


def _get_source_has_been_read(source):
    return _has_been_read_external_sources[source]


def _check_and_add_region_metadata(region):
    # Follow the hierarchy of sources
    if _set_region_metadata_from_cfg_file(region):
        logger.debug("Added metadata information for {} region from regions config file".format(region))
        return True
    elif _set_region_metadata_from_env_var(region):
        logger.debug("Added metadata information for {} region from environment variable".format(region))
        return True
    elif _set_region_from_instance_metadata_service(region):
        logger.debug("Added metadata information for {} region from IMDS".format(region))
        return True
    logger.debug("Unknown regionId '{}', will assume it's in Realm OC1".format(region))
    return False


def _set_region_metadata_from_cfg_file(region):
    # Check if region information from regions cfg file has already been read
    if _get_source_has_been_read(ExternalSources.REGIONS_CFG_FILE):
        # Return False to allow fallback
        return False

    # Set source as read
    _set_source_has_been_read(ExternalSources.REGIONS_CFG_FILE)

    expanded_file_location = os.path.expanduser(REGIONS_CONFIG_FILE_PATH)
    if os.path.isfile(expanded_file_location):
        logger.debug("Regions configuration file found")
        try:
            with open(expanded_file_location, 'r') as regions_config_file:
                regions_metadata_raw = regions_config_file.read()
        except (OSError, IOError) as e:
            logger.debug("Reading regions configuration file failed because of error: {}".format(e))
            return False

        # Try importing JSONDecodeError for Python 2 and Python 3 compatibility
        try:
            from json.decoder import JSONDecodeError
        except ImportError:
            JSONDecodeError = ValueError
        try:
            regions_metadata_array = json.loads(regions_metadata_raw)
        except JSONDecodeError as e:
            # Unable to parse the json array
            logger.debug("Decoding JSON array from regions configuration file failed because of error: {}".format(e))
            return False

        added = False
        for region_metadata in regions_metadata_array:
            if _check_valid_schema(region_metadata):
                if _add_region_information_to_lookup(region_metadata, region):
                    added = True
        return added
    return False


def _set_region_metadata_from_env_var(region):
    # Check if region information from env var has already been read
    if _get_source_has_been_read(ExternalSources.ENV_VAR):
        # Return False to allow fallback
        return False

    # Set source as read
    _set_source_has_been_read(ExternalSources.ENV_VAR)

    if os.environ.get(OCI_REGION_METADATA_ENV_VAR_NAME):
        # Try importing JSONDecodeError for Python 2 and Python 3 compatibility
        try:
            from json.decoder import JSONDecodeError
        except ImportError:
            JSONDecodeError = ValueError
        try:
            region_metadata = json.loads(os.environ.get(OCI_REGION_METADATA_ENV_VAR_NAME))
        except JSONDecodeError as e:
            # Unable to parse the env variable
            logger.debug("Decoding JSON from environment variable failed because of error: {}".format(e))
            return False

        if _check_valid_schema(region_metadata):
            return _add_region_information_to_lookup(region_metadata, region)

    return False


def _set_region_from_instance_metadata_service(region):
    # Check if region information from IMDS has already been read
    if _get_source_has_been_read(ExternalSources.IMDS):
        # Return False to allow fallback
        return False

    # Set source as read
    _set_source_has_been_read(ExternalSources.IMDS)

    try:

        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            read=0,
            connect=3,
            status=3
        )
        s = requests.Session()
        s.mount(GET_REGION_URL, HTTPAdapter(max_retries=retry_strategy))
        response = s.get(GET_REGION_URL, timeout=(10, 60), headers=METADATA_AUTH_HEADERS)
        region_metadata_raw = response.text
        logger.debug("Region metadata blob from IMDS is: {}".format(region_metadata_raw))
    except (HTTPError, ConnectionError, RetryError) as e:
        logger.debug("Failed to call IMDS service because of error: {}".format(e))
        return False

    if response.status_code != 200:
        logger.debug("HTTP Get Failed: URL: {}, Status: {}, Message: {}".format(GET_REGION_URL, response.status_code, response.text))
        return False

    try:
        from json.decoder import JSONDecodeError
    except ImportError:
        JSONDecodeError = ValueError
    try:
        region_metadata = json.loads(region_metadata_raw)
    except JSONDecodeError as e:
        # Unable to parse the raw response
        logger.debug("Decoding JSON from IMDS service because of error: {}".format(e))
        return False

    if _check_valid_schema(region_metadata):
        return _add_region_information_to_lookup(region_metadata, region)

    return False


def _check_valid_schema(region_metadata):
    for key in REGION_METADATA_KEYS:
        if key not in region_metadata:
            logger.debug("Key {} not found in region metadata".format(key))
            return False
        if region_metadata[key] == "":
            logger.debug("Value for key {} in region metadata is empty".format(key))
            return False
    return True


def _add_region_information_to_lookup(region_metadata, region):
    # Check if the region metadata has information about the requested region
    # Add the region information from region_metadata to the existing lookups
    region_metadata = {k: v.lower() for k, v in six.iteritems(region_metadata)}
    if region_metadata[REGION_KEY_PROPERTY_NAME] not in REGIONS_SHORT_NAMES:
        REGIONS_SHORT_NAMES[region_metadata[REGION_KEY_PROPERTY_NAME]] = region_metadata[REGION_IDENTIFIER_PROPERTY_NAME]

    if region_metadata[REGION_IDENTIFIER_PROPERTY_NAME] not in REGION_REALMS:
        REGION_REALMS[region_metadata[REGION_IDENTIFIER_PROPERTY_NAME]] = region_metadata[REALM_KEY_PROPERTY_NAME]

    if region_metadata[REALM_KEY_PROPERTY_NAME] not in REALMS:
        REALMS[region_metadata[REALM_KEY_PROPERTY_NAME]] = region_metadata[REALM_DOMAIN_COMPONENT_PROPERTY_NAME]

    if region_metadata[REGION_IDENTIFIER_PROPERTY_NAME] not in REGIONS:
        REGIONS.append(region_metadata[REGION_IDENTIFIER_PROPERTY_NAME])

    # Return True if the requested region is now known
    if region == region_metadata[REGION_IDENTIFIER_PROPERTY_NAME] or region == region_metadata[REGION_KEY_PROPERTY_NAME]:
        return True

    return False


def _endpoint_for(service, region=None, service_endpoint_template=None):
    # Convert short code to region identifier
    if region in REGIONS_SHORT_NAMES:
        region = REGIONS_SHORT_NAMES[region]
    # for backwards compatibility, if region already has a '.'
    # then consider it the full domain and do not append '.oraclecloud.com'
    if '.' in region:
        return _format_endpoint(service, region, service_endpoint_template)
    else:
        # get endpoint from template
        return _endpoint(service, region, service_endpoint_template)


def _endpoint(service, region, service_endpoint_template=None):
    if service_endpoint_template:
        endpoint = service_endpoint_template

        if region:
            endpoint = endpoint.replace("{region}", region)
        return endpoint.replace("{secondLevelDomain}", _second_level_domain(region))
    else:
        return _format_endpoint(service, DOMAIN_FORMAT.format(region=region, secondLevelDomain=_second_level_domain(region)))


def _second_level_domain(region):
    if region in REGION_REALMS.keys():
        realm = REGION_REALMS[region]
    else:
        # default realm to OC1
        realm = 'oc1'

    return REALMS[realm]


def _format_endpoint(service, domain, service_endpoint_template=None):
    url_format = None

    if service.lower() not in SERVICE_ENDPOINTS:
        if service_endpoint_template is None:
            raise ValueError("Unknown service {!r}".format(service))
        else:
            # If there is no entry in SERVICE_ENDPOINTS and there is
            # a service_enpoint_template attempt to convert from new service template
            # to old template.
            # From "https://service.{region}.{subdomain}" to "https://service.{domain}"
            pos = service_endpoint_template.find("{region}")
            if pos != -1:
                url_format = service_endpoint_template[:pos] + "{domain}"
    else:
        url_format = SERVICE_ENDPOINTS[service.lower()]

    if url_format is None:
        raise ValueError("Unable to format endpoint for service, {} , and service_endpoint_template, {}".format(service, service_endpoint_template))

    return url_format.format(domain=domain)
