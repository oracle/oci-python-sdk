# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import pytest
from oci._vendor import six
from oci.exceptions import ConnectTimeout, RequestException
from datetime import datetime


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


def test_deserialize_enums(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})

    # Enums are list of strings
    data = ["list", "of", "strings"]
    cls = 'EnumTypeWhichIsNotPresentInTypeMapping'
    value = client._BaseClient__deserialize(data, cls)
    # The list should be returned as is (see BaseClient.__deserialize_primitive), and code should not fail because cls is unknown
    assert value == data


def test_default_timeout(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    assert client.timeout == (10.0, 60.0)
    client = oci.BaseClient('identity', config, identity.base_client.signer, {}, timeout=(20, 70))
    assert client.timeout == (20.0, 70.0)
    client = oci.BaseClient('identity', config, identity.base_client.signer, {}, timeout=20)
    assert client.timeout == 20
    client = oci.BaseClient('identity', config, identity.base_client.signer, {}, timeout=None)
    assert client.timeout is None


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


def test_sanitize_headers_for_requests(config):

    dummy_headers = {
        "content-type": 10,
        "Content-Type": 20.0,
        "string": "string-value",
        "bool": True,
        "array": [1, 2, 3],
        "NoneHeader": None
    }
    dummy_headers = oci.base_client._sanitize_headers_for_requests(dummy_headers)

    assert isinstance(dummy_headers["content-type"], str)
    assert isinstance(dummy_headers["Content-Type"], str)
    assert isinstance(dummy_headers["string"], str)
    assert isinstance(dummy_headers["bool"], str)
    assert isinstance(dummy_headers["array"], list)
    assert isinstance(dummy_headers["array"][0], six.integer_types)
    assert isinstance(dummy_headers["NoneHeader"], type(None))


def test_get_preferred_retry_strategy(config):
    # Default case
    client = oci.identity.IdentityClient(config)

    retry_strategy = client.base_client.get_preferred_retry_strategy(operation_retry_strategy=None,
                                                                     client_retry_strategy=None)
    assert retry_strategy is None

    # Set global Retry strategy
    oci.retry.GLOBAL_RETRY_STRATEGY = oci.retry.RetryStrategyBuilder(
        backoff_type=oci.retry.BACKOFF_FULL_JITTER_VALUE).get_retry_strategy()
    retry_strategy = client.base_client.get_preferred_retry_strategy(operation_retry_strategy=None,
                                                                     client_retry_strategy=None)
    assert isinstance(retry_strategy, oci.retry.ExponentialBackoffWithFullJitterRetryStrategy)

    # Set Client retry strategy
    client_retry_strategy = oci.retry.RetryStrategyBuilder(backoff_type=oci.retry.BACKOFF_EQUAL_JITTER_VALUE).get_retry_strategy()
    retry_strategy = client.base_client.get_preferred_retry_strategy(operation_retry_strategy=None,
                                                                     client_retry_strategy=client_retry_strategy)
    assert isinstance(retry_strategy, oci.retry.ExponentialBackoffWithEqualJitterRetryStrategy)

    # Set operation level retry strategy
    operation_retry_strategy = oci.retry.RetryStrategyBuilder(
        backoff_type=oci.retry.BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE).get_retry_strategy()
    retry_strategy = client.base_client.get_preferred_retry_strategy(operation_retry_strategy=operation_retry_strategy,
                                                                     client_retry_strategy=client_retry_strategy)
    assert isinstance(retry_strategy, oci.retry.ExponentialBackoffWithFullJitterEqualForThrottlesRetryStrategy)


def test_compute_out_of_capacity_error(config):
    json_raw = r'{"code": "InternalServerError","message": "Out of host capacity.","originalMessage": "Out of capacity for shape VM.Standard2.1 in dedicated pool vmidp_stress_test.","originalMessageTemplate": "Out of capacity for shape {shape} in dedicated pool {dedicatedPool}.","messageArguments": {"problemType": "OUT_OF_CAPACITY","shape": "VM.Standard2.1","dedicatedPool": "vmidp_stress_test"}}'
    mock_response = MockResponse(content=json_raw, status_code=501, headers={'opc-request-id': 1234})

    # Default case
    client = oci.identity.IdentityClient(config)
    deserialized_data = client.base_client.deserialize_response_data(mock_response, 'object')
    assert deserialized_data['code'] == 'InternalServerError'
    with pytest.raises(oci.exceptions.ServiceError) as service_error:
        raise oci.exceptions.ServiceError(
            mock_response.status_code,
            deserialized_data['code'],
            mock_response.headers,
            deserialized_data['message'],
            deserialized_data=deserialized_data,
            target_service='Compute',
            operation_name='mock_api',
            timestamp=datetime.now().isoformat(),
            client_version='1',
            request_endpoint='www.foo.bar'
        )
    error_info = str(service_error)
    assert 'original_message' in error_info
    assert 'original_message_template' in error_info
    assert 'message_arguments' in error_info


def test_partial_compute_out_of_capacity_error(config):
    json_raw = r'{"code": "InternalServerError","message": "Out of host capacity.","messageArguments": {"problemType": "OUT_OF_CAPACITY","shape": "VM.Standard2.1","dedicatedPool": "vmidp_stress_test"}}'
    mock_response = MockResponse(content=json_raw, status_code=501, headers={'opc-request-id': 1234})

    # Default case
    client = oci.identity.IdentityClient(config)
    deserialized_data = client.base_client.deserialize_response_data(mock_response, 'object')
    assert deserialized_data['code'] == 'InternalServerError'
    with pytest.raises(oci.exceptions.ServiceError) as service_error:
        raise oci.exceptions.ServiceError(
            mock_response.status_code,
            deserialized_data['code'],
            mock_response.headers,
            deserialized_data['message'],
            deserialized_data=deserialized_data,
            target_service='Compute',
            operation_name='mock_api',
            timestamp=datetime.now().isoformat(),
            client_version='1',
            request_endpoint='www.foo.bar'
        )
    error_info = str(service_error)
    assert 'original_message' not in error_info
    assert 'original_message_template' not in error_info
    assert 'message_arguments' in error_info


def test_original_compute_out_of_capacity_error(config):
    json_raw = r'{"code": "InternalServerError","message": "Out of host capacity."}'
    mock_response = MockResponse(content=json_raw, status_code=501, headers={'opc-request-id': 1234})

    # Default case
    client = oci.identity.IdentityClient(config)
    deserialized_data = client.base_client.deserialize_response_data(mock_response, 'object')
    assert deserialized_data['code'] == 'InternalServerError'
    with pytest.raises(oci.exceptions.ServiceError) as service_error:
        raise oci.exceptions.ServiceError(
            mock_response.status_code,
            deserialized_data['code'],
            mock_response.headers,
            deserialized_data['message'],
            deserialized_data=deserialized_data,
            target_service='Compute',
            operation_name='mock_api',
            timestamp=datetime.now().isoformat(),
            client_version='1',
            request_endpoint='www.foo.bar'
        )
    error_info = str(service_error)
    assert 'code' in error_info
    assert 'original_message' not in error_info
    assert 'original_message_template' not in error_info
    assert 'message_arguments' not in error_info


class MockResponse:
    def __init__(self, content, status_code, headers):
        self.content = content
        self.status_code = status_code
        self.headers = headers

    def decode(self, format):
        return self.content
