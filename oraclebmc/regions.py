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

    Must provide only one of region """
    if service.lower() not in SERVICE_ENDPOINTS:
        raise ValueError("Unknown service {!r}".format(service))
    if not (endpoint or region):
        raise ValueError("Must supply either a region or an endpoint.")
    elif endpoint:
        # endpoint takes priority
        pass
    elif region.lower() not in REGIONS:
        raise ValueError("Unknown region {!r}".format(region))
    else:
        endpoint = REGIONS.get(region.lower())

    url_format = SERVICE_ENDPOINTS[service.lower()]
    return url_format.format(domain=endpoint)
