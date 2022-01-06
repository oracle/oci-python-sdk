# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import pytest


def test_connection_exception(identity, config):
    identity.base_client.endpoint = 'https://fakeendpoint.oracle'
    with pytest.raises(oci.exceptions.RequestException):
        identity.list_users(config['tenancy'])
