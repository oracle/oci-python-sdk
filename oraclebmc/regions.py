import six

ENDPOINTS = {
    "us-phoenix-1": {
        "identity": "https://identity.us-phoenix-1.oraclecloud.com/20160918",
        "blockstorage": "https://iaas.us-phoenix-1.oraclecloud.com/20160918",
        "compute": "https://iaas.us-phoenix-1.oraclecloud.com/20160918",
        "virtual_network": "https://iaas.us-phoenix-1.oraclecloud.com/20160918",
        "object_storage": "https://objectstorage.us-phoenix-1.oraclecloud.com",
    }
}


def get_endpoints(region_name):
    try:
        return dict(six.iteritems(ENDPOINTS[region_name.lower()]))
    except KeyError:
        raise ValueError("Unknown region {!r}".format(region_name))


def contains(region_name):
    return region_name.lower() in ENDPOINTS
