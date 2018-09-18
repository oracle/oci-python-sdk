# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from . import service_endpoints

REGIONS_SHORT_NAMES = {
    'phx': 'us-phoenix-1',
    'iad': 'us-ashburn-1',
    'fra': 'eu-frankfurt-1',
    'lhr': 'uk-london-1'
}
REGIONS = [
    "us-phoenix-1",
    "us-ashburn-1",
    "eu-frankfurt-1",
    "uk-london-1"
]
SERVICE_ENDPOINTS = service_endpoints.SERVICE_ENDPOINTS
SERVICE_ENDPOINTS['auth'] = 'https://auth.{domain}'

DOMAIN_FORMAT = "{region}.oraclecloud.com"


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
        domain = endpoint
    else:
        # no endpoint provided
        region = region.lower()

        # use service endpoint template if available
        if (service_endpoint_template):
            return service_endpoint_template.format(region=region)

        # for backwards compatibility, if region already has a '.'
        # then consider it the full domain and do not append '.oraclecloud.com'
        if '.' in region:
            domain = region
        else:
            domain = DOMAIN_FORMAT.format(region=region)

    if service.lower() not in SERVICE_ENDPOINTS:
        raise ValueError("Unknown service {!r}".format(service))

    url_format = SERVICE_ENDPOINTS[service.lower()]
    return url_format.format(domain=domain)
