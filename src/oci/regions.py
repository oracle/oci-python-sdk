# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import
import os
import json
import logging

from . import service_endpoints
from oci._vendor import six

REGIONS_SHORT_NAMES = {
    'phx': 'us-phoenix-1',
    'iad': 'us-ashburn-1',
    'fra': 'eu-frankfurt-1',
    'zrh': 'eu-zurich-1',
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
    'hyd': 'ap-hyderabad-1'
}
REGION_REALMS = {
    'ap-melbourne-1': 'oc1',
    'ap-mumbai-1': 'oc1',
    'ap-hyderabad-1': 'oc1',
    'ap-osaka-1': 'oc1',
    'ap-seoul-1': 'oc1',
    'ap-sydney-1': 'oc1',
    'ap-tokyo-1': 'oc1',
    'us-phoenix-1': 'oc1',
    'us-ashburn-1': 'oc1',
    'eu-amsterdam-1': 'oc1',
    'eu-frankfurt-1': 'oc1',
    'eu-zurich-1': 'oc1',
    'me-jeddah-1': 'oc1',
    'uk-london-1': 'oc1',
    'ca-toronto-1': 'oc1',
    'sa-saopaulo-1': 'oc1',
    'ca-montreal-1': 'oc1',

    'us-langley-1': 'oc2',
    'us-luke-1': 'oc2',

    'us-gov-ashburn-1': 'oc3',
    'us-gov-chicago-1': 'oc3',
    'us-gov-phoenix-1': 'oc3',

    'uk-gov-london-1': 'oc4'
}
REALMS = {
    'oc1': 'oraclecloud.com',
    'oc2': 'oraclegovcloud.com',
    'oc3': 'oraclegovcloud.com',
    'oc4': 'oraclegovcloud.uk'
}
REGIONS = [
    "ap-melbourne-1",
    "ap-mumbai-1",
    "ap-hyderabad-1",
    "ap-osaka-1",
    "ap-seoul-1",
    "ap-sydney-1",
    "ap-tokyo-1",
    "us-phoenix-1",
    "us-ashburn-1",
    "eu-amsterdam-1",
    "eu-frankfurt-1",
    "eu-zurich-1",
    "me-jeddah-1",
    "uk-london-1",
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

REGION_METADATA_KEYS = (REALM_KEY_PROPERTY_NAME,
                        REALM_DOMAIN_COMPONENT_PROPERTY_NAME,
                        REGION_KEY_PROPERTY_NAME,
                        REGION_IDENTIFIER_PROPERTY_NAME)

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
        logger.info("Could not find region information in lookups and any other sources")
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
        logger.info("Cannot find region information in lookups and other sources, defaulting to OC1 realm")
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

    The region metadata schema is:
    {
        "realmKey" : string,
        "realmDomainComponent" : string,
        "regionKey" : string,
        "regionIdentifier" : string
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


def _check_and_add_region_metadata(region):
    region = region.lower()
    # Follow the hierarchy of sources
    if _set_region_metadata_from_cfg_file(region):
        return True
    elif _set_region_metadata_from_env_var(region):
        return True
    elif _set_region_from_instance_metadata_service(region):
        return True
    return False


def _set_region_metadata_from_cfg_file(region):
    return False


def _set_region_metadata_from_env_var(region):
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
            logger.debug("Decoding JSON failed because of error: {}".format(e))
            return False

        if _check_valid_schema(region_metadata):
            region_metadata = {k: v.lower() for k, v in six.iteritems(region_metadata)}
            return _add_region_information_to_lookup(region_metadata, region)

    return False


def _set_region_from_instance_metadata_service(region):
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
