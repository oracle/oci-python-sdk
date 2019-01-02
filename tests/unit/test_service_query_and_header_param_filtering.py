# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
import pytest


# A dummy client where we have shoved in our BaseDummyClient to intercept the
# args and kwargs passed to BaseClient.call_api() and also disabled the retry
# strategy (since we'll never make an actual call)
@pytest.fixture
def dummy_service_client(config):
    compute_client = oci.core.ComputeClient(config)
    compute_client.retry_strategy = None
    compute_client.base_client = DummyBaseClient()
    return compute_client


def test_none_query_params_filtered_out(dummy_service_client):
    result = dummy_service_client.list_images(
        'fake_compartment_id',
        display_name=None,
        operating_system='fake value',
        operating_system_version=oci.util.NONE_SENTINEL
    )

    assert len(result.query_params) == 3
    assert result.query_params['operatingSystem'] == 'fake value'
    assert result.query_params['operatingSystemVersion'] is oci.util.NONE_SENTINEL
    assert 'displayName' not in result.query_params


def test_none_header_params_filtered_out(dummy_service_client):
    result = dummy_service_client.instance_action(
        'fake_instance_id',
        'start',
        opc_retry_token=None,
        if_match='blah'
    )
    assert len(result.header_params) == 3
    assert result.header_params['if-match'] == 'blah'
    assert 'opc-retry-token' not in result.header_params

    result = dummy_service_client.instance_action(
        'fake_instance_id',
        'start',
        opc_retry_token=oci.util.NONE_SENTINEL
    )
    assert len(result.header_params) == 3
    assert result.header_params['opc-retry-token'] is oci.util.NONE_SENTINEL
    assert 'if-match' not in result.header_params


# Could use a mock, this seemed a bit more lightweight
class DummyBaseClient(object):
    def __init__(self):
        self.query_params = None
        self.header_params = None

    def call_api(self, *args, **kwargs):
        self.query_params = kwargs.get('query_params')
        self.header_params = kwargs.get('header_params')
        return self
