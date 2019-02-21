# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from . import service_endpoints

REGIONS_SHORT_NAMES = {
    'phx': 'us-phoenix-1',
    'iad': 'us-ashburn-1',
    'fra': 'eu-frankfurt-1',
    'lhr': 'uk-london-1',
    'yyz': 'ca-toronto-1'
}
REGION_REALMS = {
    'us-phoenix-1': 'oc1',
    'us-ashburn-1': 'oc1',
    'eu-frankfurt-1': 'oc1',
    'uk-london-1': 'oc1',
    'ca-toronto-1': 'oc1',

    'us-langley-1': 'oc2',
    'us-luke-1': 'oc2',

    'us-gov-ashburn-1': 'oc3',
    'us-gov-chicago-1': 'oc3',
    'us-gov-phoenix-1': 'oc3'
}
REALMS = {
    'oc1': 'oraclecloud.com',
    'oc2': 'oraclegovcloud.com',
    'oc3': 'oraclegovcloud.com'
}
REGIONS = [
    "us-phoenix-1",
    "us-ashburn-1",
    "eu-frankfurt-1",
    "uk-london-1",
    "ca-toronto-1",
    "us-langley-1",
    "us-luke-1",
    "us-gov-ashburn-1",
    "us-gov-chicago-1",
    "us-gov-phoenix-1"
]
SERVICE_ENDPOINTS = service_endpoints.SERVICE_ENDPOINTS
SERVICE_ENDPOINTS['auth'] = 'https://auth.{domain}'

DOMAIN_FORMAT = "{region}.{secondLevelDomain}"


def is_region(region_name):
    return region_name.lower() in REGIONS


def endpoint_for(service, region=None, endpoint=None, service_endpoint_template=None):
    """Returns the base URl for a service, either in the given region or at the specified endpoint.

    If endpoint and region are provided, endpoint is used.
    """
    if not (endpoint or region):
        raise ValueError("Must supply either a region or an endpoint.")
    elif endpoint:
        # endpoint takes priority
        return _format_endpoint(service, endpoint)
    else:
        # no endpoint provided
        region = region.lower()

        # for backwards compatibility, if region already has a '.'
        # then consider it the full domain and do not append '.oraclecloud.com'
        if '.' in region:
            return _format_endpoint(service, region)
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


def _format_endpoint(service, domain):
    if service.lower() not in SERVICE_ENDPOINTS:
        raise ValueError("Unknown service {!r}".format(service))

    url_format = SERVICE_ENDPOINTS[service.lower()]
    return url_format.format(domain=domain)
