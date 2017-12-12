# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .service_endpoints import SERVICE_ENDPOINTS

REGIONS = [
    "us-phoenix-1",
    "us-ashburn-1",
    "eu-frankfurt-1"
]
SERVICE_ENDPOINTS = SERVICE_ENDPOINTS

DOMAIN_FORMAT = "{region}.oraclecloud.com"


def is_region(region_name):
    return region_name.lower() in REGIONS


def endpoint_for(service, region=None, endpoint=None):
    """Returns the base URl for a service, either in the given region or at the specified endpoint.

    If endpoint and region are provided, endpoint is used.
    """
    if service.lower() not in SERVICE_ENDPOINTS:
        raise ValueError("Unknown service {!r}".format(service))

    if not (endpoint or region):
        raise ValueError("Must supply either a region or an endpoint.")
    elif endpoint:
        # endpoint takes priority
        domain = endpoint
    else:
        # no endpoint provided
        region = region.lower()

        # for backwards compatibility, if region already has a '.'
        # then consider it the full domain and do not append '.oraclecloud.com'
        if '.' in region:
            domain = region
        else:
            domain = DOMAIN_FORMAT.format(region=region)

    url_format = SERVICE_ENDPOINTS[service.lower()]
    return url_format.format(domain=domain)
