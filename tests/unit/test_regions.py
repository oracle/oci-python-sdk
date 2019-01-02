# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from oci.regions import endpoint_for


def test_endpoint_for_service_template():
    # set region template
    endpoint = endpoint_for('blockstorage', 'foo_region', None, 'https://{region}.bar.com')
    assert endpoint == 'https://foo_region.bar.com'

    # no template
    endpoint = endpoint_for('blockstorage', 'us-foo_region-1', None, None)
    assert endpoint == 'https://iaas.us-foo_region-1.oraclecloud.com'

    # second level domain template
    endpoint = endpoint_for('blockstorage', 'us-foo_region-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclecloud.com'


def test_endpoint_for_endpoint():
    # only endpoint set
    endpoint = endpoint_for('compute', None, 'endpoint', None)
    assert endpoint == 'https://iaas.endpoint'

    # both endpoint and region set, then endpoint should take over
    endpoint = endpoint_for('compute', 'us-foo_region-1', 'endpoint', None)
    assert endpoint == 'https://iaas.endpoint'


def test_endpoint_for_region():
    endpoint = endpoint_for('compute', 'us-phoenix-1', None, None)
    assert endpoint == 'https://iaas.us-phoenix-1.oraclecloud.com'

    # region contains dot
    endpoint = endpoint_for('compute', '.us-phoenix-1', 'test.com', None)
    assert endpoint == 'https://iaas.test.com'

    endpoint = endpoint_for('compute', 'us-phoenix-1.oraclecloud.com', None, None)
    assert endpoint == 'https://iaas.us-phoenix-1.oraclecloud.com'
