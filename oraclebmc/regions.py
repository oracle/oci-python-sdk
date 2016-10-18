import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

REGIONS = {
    "us-phoenix-1": "us-phoenix-1.oraclecloud.com"
}
SERVICE_ENDPOINTS = {
    "identity": "https://identity.{domain}/20160918",
    "blockstorage": "https://iaas.{domain}/20160918",
    "compute": "https://iaas.{domain}/20160918",
    "virtual_network": "https://iaas.{domain}/20160918",
    "object_storage": "https://objectstorage.{domain}"
}


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
        region = region.lower()
        # no endpoint provided; use region, warn if unknown
        if region not in REGIONS:
            logger.warn("Using unknown region '%s' to build service endpoint for '%s'", region, service)
        domain = REGIONS.get(region, region)

    url_format = SERVICE_ENDPOINTS[service.lower()]
    return url_format.format(domain=domain)
