# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import pytest
from oci.exceptions import ConnectTimeout, RequestException


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

    assert isinstance(err.value, oci.exceptions.MissingEndpointForNonRegionalServiceClientError)
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


def test_deserialize_datetime(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    ddt = client._BaseClient__deserialize_datetime('2018-11-30T18:49:58.825Z')
    assert ddt.tzinfo is not None


def test_default_timeout(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    assert client.timeout == (10.0, 60.0)
    client = oci.BaseClient('identity', config, identity.base_client.signer, {}, timeout=(20, 70))
    assert client.timeout == (20.0, 70.0)
    client = oci.BaseClient('identity', config, identity.base_client.signer, {}, timeout=20)
    assert client.timeout == 20


def test_default_timeout_service_client(config):
    # Test to check if values are propagated from service client to the base client

    # Default case
    client = oci.identity.IdentityClient(config)
    assert client.base_client.timeout == (10.0, 60.0)

    # Assert if custom timeout values are propagated to the base client
    client = oci.identity.IdentityClient(config, timeout=(20, 70))
    assert client.base_client.timeout == (20, 70)

    # Assert if custom timeout values are propagated all the way to the requests
    client = oci.identity.IdentityClient(config, timeout=0.0001)
    with pytest.raises((ConnectTimeout, RequestException), match=r".* timed out.*"):
        client.list_regions()
