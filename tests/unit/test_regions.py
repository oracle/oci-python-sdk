# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from oci.regions import endpoint_for, REGIONS_SHORT_NAMES, REGIONS, REGION_REALMS, REALMS
from oci._vendor import six


def test_endpoint_for_service_template():
    # set region template
    endpoint = endpoint_for('blockstorage', 'foo_region', None, 'https://{region}.bar.com')
    assert endpoint == 'https://foo_region.bar.com'

    # no template
    endpoint = endpoint_for('blockstorage', 'us-foo_region-1', None, None)
    assert endpoint == 'https://iaas.us-foo_region-1.oraclecloud.com'

    # second level domain template with unknown region
    endpoint = endpoint_for('blockstorage', 'us-foo_region-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclecloud.com'

    # second level domain template with oc1 region
    endpoint = endpoint_for('blockstorage', 'us-phoenix-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclecloud.com'

    # second level domain template with oc2 region
    endpoint = endpoint_for('blockstorage', 'us-langley-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclegovcloud.com'

    # second level domain template with oc3 region
    endpoint = endpoint_for('blockstorage', 'us-gov-ashburn-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclegovcloud.com'


def test_endpoint_for_endpoint():
    # only endpoint set
    endpoint = endpoint_for('compute', None, 'endpoint', None)
    assert endpoint == 'https://iaas.endpoint'

    # both endpoint and region set, then endpoint should take over
    endpoint = endpoint_for('compute', 'us-foo_region-1', 'endpoint', None)
    assert endpoint == 'https://iaas.endpoint'


def test_endpoint_for_region():
    # oc1
    endpoint = endpoint_for('compute', 'us-phoenix-1', None, None)
    assert endpoint == 'https://iaas.us-phoenix-1.oraclecloud.com'

    # oc2
    endpoint = endpoint_for('compute', 'us-langley-1', None, None)
    assert endpoint == 'https://iaas.us-langley-1.oraclegovcloud.com'

    # oc3
    endpoint = endpoint_for('compute', 'us-gov-ashburn-1', None, None)
    assert endpoint == 'https://iaas.us-gov-ashburn-1.oraclegovcloud.com'

    # region contains dot
    endpoint = endpoint_for('compute', '.us-phoenix-1', 'test.com', None)
    assert endpoint == 'https://iaas.test.com'

    endpoint = endpoint_for('compute', 'us-phoenix-1.oraclecloud.com', None, None)
    assert endpoint == 'https://iaas.us-phoenix-1.oraclecloud.com'


def test_short_name_to_region():
    for shortname in six.iterkeys(REGIONS_SHORT_NAMES):
        assert(REGIONS_SHORT_NAMES[shortname] in REGIONS)


def test_short_name_to_realm():
    for shortname in six.iterkeys(REGIONS_SHORT_NAMES):
        assert(REGIONS_SHORT_NAMES[shortname] in REGION_REALMS)


def test_region_to_realm():
    for region in REGIONS:
        assert(region in REGION_REALMS)
        assert(REGION_REALMS[region] in REALMS)