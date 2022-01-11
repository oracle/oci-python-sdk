# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci


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
