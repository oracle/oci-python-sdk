# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
import pytest


def test_identity_list_users(identity, config):
    response = identity.list_users(config["tenancy"])

    assert response is not None
    assert len(response.data) > 0
    assert type(response.data[0]) is oci.identity.models.User
    assert response.status == 200
    assert response.request_id is not None


def test_vcn_list_vcns(virtual_network, config):
    response = virtual_network.list_vcns(config["tenancy"])

    assert response is not None
    assert response.status == 200
    assert response.request_id is not None


def test_vcn_list_instances(compute, config):
    response = compute.list_instances(config["tenancy"])

    assert response is not None
    assert response.status == 200
    assert response.request_id is not None


def test_limit(identity, config):
    response = identity.list_users(config["tenancy"], limit=1)

    assert response is not None
    assert len(response.data) == 1
    assert type(response.data[0]) is oci.identity.models.User
    assert response.status == 200
    assert response.request_id is not None


def test_api_call_with_explicit_timeout(config):
    client = oci.identity.IdentityClient(config)

    # Test connection timeout
    client.base_client.timeout = 0.01  # 0.01s timeout on connection and read. Should be too short to connect without timing out
    with pytest.raises(oci.exceptions.ConnectTimeout):
        client.list_users(config['tenancy'])
        assert False

    # Test read timeout
    client.base_client.timeout = (1, 0.01)  # 1s timeout on connection, 0.01s on read. Should be too short read
    with pytest.raises(oci.exceptions.RequestException):
        client.list_users(config['tenancy'])
        assert False

    client.base_client.timeout = 5
    response = client.list_users(config['tenancy'])
    assert len(response.data) > 0
