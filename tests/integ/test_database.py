# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import pytest
from oci._vendor import six


# basic smoke tests that db service is working, more in depth testing is covered in the CLI
def test_list_db_systems(config, database_client):
    response = database_client.list_db_systems(config['tenancy'])
    assert response.status == 200


@pytest.mark.skip(reason="re-enable after the breaking generated changes merged in")
def test_list_db_shapes(config, database_client):
    response = database_client.list_db_system_shapes(config['tenancy'])
    assert response.status == 200
    assert len(response.data) > 0
    for db_system_shape_summary in response.data:
        for attribute_name in six.iterkeys(db_system_shape_summary.swagger_types):
            # It is possible for core_count_increment to be 0, so a straight assertion on
            # getattr would not work
            assert getattr(db_system_shape_summary, attribute_name) is not None
