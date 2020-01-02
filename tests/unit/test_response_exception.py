# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

import oci
import pytest


def test_connection_exception(identity, config):
    identity.base_client.endpoint = 'https://fakeendpoint.oracle'
    with pytest.raises(oci.exceptions.RequestException):
        identity.list_users(config['tenancy'])
