# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import oci
import pytest


# Note: the identity client is passed here because I'm too lazy to create a new signer
def test_regional_client_does_not_need_explicit_endpoint(identity, config):
    assert 'endpoint' not in config
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    assert client.endpoint == oci.regions.endpoint_for('identity', config['region'])


def test_regional_client_honours_explicit_endpoint(identity, config):
    assert 'endpoint' not in config
    client = oci.BaseClient('identity', config, identity.base_client.signer, {}, service_endpoint='https://my.fake.endpoint')
    assert client.endpoint == 'https://my.fake.endpoint'


def test_non_regional_client_no_endpoint(identity, config):
    with pytest.raises(ValueError) as err:
        oci.BaseClient('identity', config, identity.base_client.signer, {}, regional_client=False)
    assert 'An endpoint must be provided for a non-regional service client' == str(err.value)


def test_non_regional_endpoint_honours_explicit_endpoint(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {}, regional_client=False, service_endpoint='https://fake.point')
    assert client.endpoint == 'https://fake.point'


def test_base_path_appended_if_not_in_endpoint_explicit_endpoint(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {}, service_endpoint='https://my.fake.endpoint', base_path='/20160918')
    assert client.endpoint == 'https://my.fake.endpoint/20160918'
    assert client._base_path == '/20160918'


def test_base_path_not_appended_if_in_endpoint_explicit_endpoint(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {}, service_endpoint='https://my.fake.endpoint/20160918', base_path='/20160918')
    assert client.endpoint == 'https://my.fake.endpoint/20160918'
    assert client._base_path == '/20160918'


def test_path_path_not_appended_if_in_endpoint_no_explicit_endpoint(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {}, base_path='/20160918')
    if oci.regions.endpoint_for('identity', region=config['region']).endswith('/20160918'):
        assert client.endpoint == oci.regions.endpoint_for('identity', region=config['region'])
    else:
        assert client.endpoint == '{}{}'.format(oci.regions.endpoint_for('identity', region=config['region']), '/20160918')


def test_service_endpoint_template(identity, config):
    service_endpoint_template = 'https://foobar.{region}.oci.oraclecloud.com'
    client = oci.BaseClient('foobar', config, identity.base_client.signer, {}, service_endpoint_template=service_endpoint_template)
    assert client.endpoint == service_endpoint_template.format(region=config['region'])
    region_london = 'uk-london-1'
    client.set_region(region_london)
    assert client.endpoint == service_endpoint_template.format(region=region_london)
